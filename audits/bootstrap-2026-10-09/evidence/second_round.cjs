const fs=require('fs'),path=require('path'),vm=require('vm');
const {chromium}=require('/Users/selcuk/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
(async()=>{
 const src=fs.readFileSync('blog/bootstrap/index.html','utf8');
 const start=src.indexOf('function lgamma('),end=src.indexOf('/* ================= Figure 1:');
 const ctx={};vm.createContext(ctx);vm.runInContext(src.slice(start,end),ctx);
 const exact={};for(const key of ['table','outlier'])for(const stat of ['mean','median']){
  const e=ctx.exactFor(key,stat); exact[key+':'+stat]={probabilitySum:Array.from(e.D.p).reduce((a,b)=>a+b,0),...Object.fromEntries(Object.entries(e).filter(([k])=>!['D','prog'].includes(k)))};
 }
 const input=JSON.parse(fs.readFileSync(path.join(__dirname,'checks.json')));const hashes={};
 const crypto=require('crypto');for(const [file,expected]of Object.entries(input.input_sha256)){hashes[file]=crypto.createHash('sha256').update(fs.readFileSync(file)).digest('hex')===expected;}
 const b=await chromium.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'});
 const p=await b.newPage(); const copied=[];
 await p.addInitScript(()=>{window.__copied=[];Object.defineProperty(navigator,'clipboard',{configurable:true,value:{writeText:async text=>{window.__copied.push(text);}}});});
 await p.goto('file://'+path.resolve('blog/bootstrap/index.html'));
 await p.locator('[data-pt-copy-md]').first().click();await p.waitForFunction(()=>window.__copied.length>0);
 const offlineCopy=await p.evaluate(()=>({length:window.__copied[0].length,status:document.querySelector('.pt-status')?.textContent,embeddedLength:document.querySelector('#pt-md').value.length}));
 await b.close();const result={exact,sourceUnchanged:hashes,offlineCopy};fs.writeFileSync(path.join(__dirname,'second-round.json'),JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify(result,null,2));
})().catch(e=>{console.error(e);process.exit(1)});
