const fs = require('fs'), path = require('path');
const {chromium} = require('/Users/selcuk/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
(async()=>{
 const out = __dirname, url='file://'+path.resolve('blog/bootstrap/index.html');
 const browser = await chromium.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'});
 const results={};
 for(const width of [1280,375]) {
  const page=await browser.newPage({viewport:{width,height:1000},colorScheme:'light'}); const errors=[];
  page.on('pageerror',e=>errors.push(String(e)));
  await page.goto(url,{waitUntil:'load'}); await page.evaluate(()=>document.fonts.ready);
  const states={};
  async function record(fig,name){states[name]=await page.locator('#fig'+fig).evaluate(svg=>{
   const vb=svg.viewBox.baseVal;const texts=[...svg.querySelectorAll('text')].map(t=>{const b=t.getBBox();return {t:t.textContent,x:b.x,y:b.y,w:b.width,h:b.height};});
   const clipped=texts.filter(t=>t.x < -0.5 || t.y < -0.5 || t.x+t.w>vb.width+.5 || t.y+t.h>vb.height+.5);
   const overlapping=[];for(let i=0;i<texts.length;i++)for(let j=i+1;j<texts.length;j++){const a=texts[i],b=texts[j];if(a.x<b.x+b.w-1&&b.x<a.x+a.w-1&&a.y<b.y+b.h-1&&b.y<a.y+a.h-1)overlapping.push([a.t,b.t]);}
   return {aria:svg.getAttribute('aria-label'),clipped,overlapping};
  });}
  for(let f=1;f<=3;f++)await record(f,'f'+f+'-initial');
  if(width===1280){
   for(const [i,name]of [[0,'once'],[0,'twice'],[1,'hundred'],[2,'thousand'],[3,'ideal'],[4,'reset']]){await page.locator('#f1-acts button').nth(i).click();await record(1,'f1-'+name);}
   for(let d=0;d<2;d++)for(let s=0;s<2;s++){await page.locator('#f2-data button').nth(d).click();await page.locator('#f2-stat button').nth(s).click();await record(2,`f2-${d}-${s}`);}
   for(let p=0;p<2;p++)for(let n=0;n<4;n++)for(let m=0;m<4;m++){
    await page.locator('#f3-pop button').nth(p).click();await page.locator('#f3-n button').nth(n).click();await page.locator('#f3-m button').nth(m).click();await record(3,`f3-${p}-${[5,10,20,40][n]}-${m}`);
   }
  }
  await page.screenshot({path:path.join(out,`browser-${width}.png`),fullPage:true});
  results[width]={states,errors,overflow:await page.evaluate(()=>({client:document.documentElement.clientWidth,scroll:document.documentElement.scrollWidth}))};
  await page.close();
 }
 await browser.close();fs.writeFileSync(path.join(out,'browser.json'),JSON.stringify(results,null,2)+'\n');
 console.log(JSON.stringify(Object.fromEntries(Object.entries(results).map(([w,r])=>[w,{states:Object.keys(r.states).length,errors:r.errors,overflow:r.overflow,issues:Object.entries(r.states).filter(([,s])=>s.clipped.length||s.overlapping.length)}])),null,2));
})().catch(e=>{console.error(e);process.exit(1)});
