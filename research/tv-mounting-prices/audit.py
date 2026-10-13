import re, json, os, sys, html, itertools
SITE="/home/claude/abstract-enterprises-site"; BP=os.path.dirname(os.path.abspath(__file__))
ALL=sys.argv[1].split(','); NEW=sys.argv[2].split(',')
GB={'nyc':'Troy','long-island':'Troy','hudson-valley':'Fordham','manhattan':'Fordham','brooklyn':'Troy','queens':'Fordham','bronx':'Fordham','staten-island':'Troy',
    'nassau-county':'Troy','suffolk-county':'Troy'}
def txt(s): return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',re.sub(r'<(script|style)[^>]*>.*?</\1>',' ',s,flags=re.S))))
def nq(q): return re.sub(r'[^a-z0-9 ]','',html.unescape(re.sub('<[^>]+>','',q)).lower()).strip()
out=[]; sizes={}; Q={}
for k in ALL:
    f=os.path.join(SITE,'tv-mounting-prices-%s.html'%k); s=open(f,encoding='utf-8').read(); sizes[k]=len(s.encode())
    D=json.load(open(os.path.join(BP,k+'.json'))); Q[k]=set(nq(x['q']) for x in D['qa']+D['faq'])
    if k not in NEW: continue
    t=re.search(r'<title>(.*?)</title>',s).group(1); md=re.search(r'<meta name="description" content="([^"]*)"',s).group(1)
    can=re.search(r'<link rel="canonical" href="([^"]*)"',s).group(1)
    w=len(txt(s[s.index('<body'):]).split())
    fq=[x for x in re.findall(r'<script type="application/ld\+json">(.*?)</script>',s,re.S) if '"FAQPage"' in x]
    nf=len(json.loads(fq[0])['mainEntity'])
    foot=s[s.index('<footer'):]
    chk=dict(title=len(html.unescape(t))<=60, meta=150<=len(html.unescape(md))<=160, canon=can.endswith('/tv-mounting-prices-'+k) and 'www.' in can,
             h1=s.count('<h1')==1, words=w>=2500, gbp=GB[k] in foot, faq=nf==len(D['faq']), stats='Monthly Fees' in s and 'Same-Day Estimates' in s,
             fresh='Updated October 13, 2026' in s, noindex='noindex' not in s, onenav='mega-nav.js' in s, calc='aessTvCalc' in s,
             qa_faq=not (set(nq(x['q']) for x in D['qa']) & set(nq(x['q']) for x in D['faq'])))
    out.append('== %s  title=%d meta=%d words=%d faq=%d  %s'%(k,len(html.unescape(t)),len(html.unescape(md)),w,nf,' '.join(('%s:%s'%(a,'PASS' if b else 'FAIL')) for a,b in chk.items())))
    links=sorted(set(re.findall(r'href="/(tv-[a-z-]+)"',s))); out.append('   links: '+' '.join(links))
for a,b in itertools.combinations(ALL,2):
    if a in NEW or b in NEW:
        g=abs(sizes[a]-sizes[b]); d=len(Q[a]&Q[b])
        if g<=2048 or d: out.append('FLAG %s/%s gap=%d dupQ=%d %s'%(a,b,g,d,list(Q[a]&Q[b])[:3]))
out.append('sizes '+str(sizes))
print('\n'.join(out))
