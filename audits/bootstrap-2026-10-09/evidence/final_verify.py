from pathlib import Path
import hashlib,json,re,html,math
root=Path(__file__).resolve().parents[3]
evidence=Path(__file__).resolve().parent
report=(evidence.parent/'REVIEW.md').read_text()
source=(root/'blog/bootstrap/index.html').read_text()
checks=json.loads((evidence/'checks.json').read_text())
round2=json.loads((evidence/'second-round.json').read_text())
findings=re.findall(r'^### (F\d+) — ',report,re.M)
assert findings==['F1','F2','F3','F4','F5']
for f,h in checks['input_sha256'].items():assert hashlib.sha256((root/f).read_bytes()).hexdigest()==h,f
assert all(round2['sourceUnchanged'].values())
assert round2['offlineCopy']['length']==round2['offlineCopy']['embeddedLength']==0
for name,expected in {'table:mean':(3.158005699804862,[1.3,13.7]),'outlier:mean':(4.552471856036013,[1.8,19.5])}.items():
 actual=round2['exact'][name];assert abs(actual['se']-expected[0])<1e-12;assert all(abs(a-b)<1e-12 for a,b in zip(actual['perc'],expected[1]))
for v in round2['exact'].values():assert abs(v['probabilitySum']-1)<1e-12
rows=json.loads((evidence/'coverage-summary.json').read_text())
for r in rows:
 assert r['trials']==10000
 label='Normal' if r['pop']=='normal' else 'Lognormal'
 vals=[f"{r['coverage_pct'][k]:.2f}" for k in ['t','perc','bca','boott']]
 assert '| '+label+' | '+str(r['n'])+' | '+' | '.join(vals)+' |' in report
 # Check source table's integer-percent cells independently of report table.
 tbl=re.search(r'<caption><b>Table 3\.</b>(.*?)</table>',source,re.S)[1]
 pat=r'<tr><td>'+('Normal' if label=='Normal' else 'Skewed')+r'</td><td class="r">'+str(r['n'])+r'</td>(.*?)</tr>'
 cells=re.findall(r'>(\d+)%<',re.search(pat,tbl,re.S)[1])
 assert [int(x) for x in cells]==[round(r['coverage_pct'][k]) for k in ['t','perc','bca','boott']],(r,cells)
# Every explicit quote of article wording in the findings is present in primary HTML.
for quoted in ['Copy as Markdown','Ideal']:
 assert quoted in source
assert 'provided the model fits and the variance is constant' in source
assert 'provided the model fits and the variance is constant' not in (root/'blog/bootstrap/index.md').read_text()
assert 'Persistent review and verification rule' in (root/'AGENTS.md').read_text()
assert 'No new findings in this reviewed scope' in report
result={'findings':len(findings),'source_hashes_unchanged':True,'coverage_table_and_report_agree':True,'exact_js_python_agree':True,'offline_copy_failure_confirmed':True,'final_full_scope_round':'no new findings; recorded article findings remain open'}
(evidence/'final-verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
