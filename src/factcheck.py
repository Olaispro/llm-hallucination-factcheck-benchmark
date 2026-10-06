"""Aggregate human-adjudicated evidence labels; no automatic truth claims."""
import argparse,json,collections
LABELS={'supported','contradicted','not_enough_evidence'}
def summarize(rows):
    counts=collections.Counter(r['label'] for r in rows)
    bad=[r for r in rows if r.get('label') not in LABELS]
    n=len(rows)-len(bad)
    return {'claims_total':len(rows),'valid_labels':n,'invalid_rows':len(bad),'counts':dict(counts),
      'unsupported_rate':round((counts['contradicted']+counts['not_enough_evidence'])/n,3) if n else None,
      'coverage_rate':round(counts['supported']/n,3) if n else None,
      'note':'Unsupported includes contradicted and not-enough-evidence claims; inspect each claim and its cited evidence.'}
def main():
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('--out',default='factcheck-report.json');a=p.parse_args();rows=[json.loads(x) for x in open(a.input,encoding='utf-8') if x.strip()];r=summarize(rows);open(a.out,'w',encoding='utf-8').write(json.dumps(r,indent=2));print(json.dumps(r,indent=2))
if __name__=='__main__':main()
