import sys, json, re, html, os
sys.path.insert(0, '/tmp/claude-0/-home-claude/79c6f0e5-974d-5a24-9def-72172566d30a/scratchpad')
from nb import NB, LOGI, ROOMS
from newpages import sec, p, cards, faq, T, BASE, strip, FI

SITE = "/home/claude/abstract-enterprises-site"
BP = os.path.dirname(os.path.abspath(__file__))
TODAY = "2026-10-13"

HUBS = {
 'nyc': dict(name='NYC', place='New York City', zone='nyc', base=179.99, hourly=195, gbp='brooklyn', svc='tv-installation-nyc',
   areas=[('Brooklyn &amp; Queens', 179.99), ('The Bronx &amp; Staten Island', 209.99), ('Manhattan (plus $150 parking)', 244.99)],
   kids=[('manhattan', 'Manhattan', 'tv-installation-manhattan'), ('brooklyn', 'Brooklyn', 'tv-installation-brooklyn'), ('queens', 'Queens', 'tv-installation-queens'),
         ('bronx', 'the Bronx', 'tv-installation-bronx'), ('staten-island', 'Staten Island', 'tv-installation-staten-island')],
   kids_title='TV Mounting Prices in Every NYC Borough'),
 'long-island': dict(name='Long Island', place='Long Island', zone='longisland', base=209.99, hourly=225, gbp='brooklyn', svc='tv-installation-long-island',
   areas=[('Nassau County', 209.99), ('Suffolk County', 229.99)],
   kids=[('nassau-county', 'Nassau County', 'tv-installation-nassau-county'), ('suffolk-county', 'Suffolk County', 'tv-installation-suffolk-county')],
   kids_title='TV Mounting Prices Across Long Island'),
 'hudson-valley': dict(name='Hudson Valley', place='the Hudson Valley', zone='hudsonvalley', base=219.99, hourly=235, gbp='bronx', svc='tv-installation-hudson-valley',
   areas=[('Westchester &amp; Rockland', 219.99), ('Orange &amp; Putnam', 229.99), ('Dutchess &amp; Ulster', 254.99)],
   kids=[('westchester-county', 'Westchester', 'tv-installation-westchester-county'), ('rockland-county', 'Rockland', 'tv-installation-rockland-county'),
         ('orange-county', 'Orange County', 'tv-installation-orange-county'), ('putnam-county', 'Putnam', 'tv-installation-putnam-county'),
         ('dutchess-county', 'Dutchess', 'tv-installation-dutchess-county'), ('ulster-county', 'Ulster', 'tv-installation-ulster-county')],
   kids_title='TV Mounting Prices in Every Hudson Valley County'),
}

NYC_SIB=[('manhattan','Manhattan',244.99,265,'manhattan','bronx'),('brooklyn','Brooklyn',179.99,195,'brooklyn','brooklyn'),('queens','Queens',179.99,195,'queens','bronx'),
         ('bronx','the Bronx',209.99,225,'bronx','bronx'),('staten-island','Staten Island',209.99,225,'statenisland','brooklyn')]
LI_SIB=[('nassau-county','Nassau County',209.99,225,'nassau','brooklyn'),('suffolk-county','Suffolk County',229.99,250,'suffolk','brooklyn')]
HV_SIB=[('westchester-county','Westchester County',219.99,235,'westchester','bronx'),('rockland-county','Rockland County',219.99,235,'rockland','bronx'),
        ('orange-county','Orange County',229.99,250,'orange','bronx'),('putnam-county','Putnam County',229.99,250,'putnam','bronx'),
        ('dutchess-county','Dutchess County',254.99,275,'dutchess','bronx'),('ulster-county','Ulster County',254.99,275,'ulster','bronx')]
SPOKES={}
for parent, sib, title in (('nyc',NYC_SIB,'TV Mounting Prices in the Other NYC Boroughs'),('long-island',LI_SIB,'TV Mounting Prices Elsewhere on Long Island'),
                           ('hudson-valley',HV_SIB,'TV Mounting Prices in Other Hudson Valley Counties')):
    for kk,nm,bs,hr,zn,gb in sib:
        SPOKES[kk]=dict(name=nm[4:].capitalize() if nm.startswith('the ') else nm, place=nm, zone=zn, base=bs, hourly=hr, gbp=gb,
            svc='tv-installation-'+kk, areas=[(nm[0].upper()+nm[1:], bs)], parent=parent,
            kids=[(a, b, 'tv-installation-'+a) for a,b,*_ in sib if a!=kk], kids_title=title)
SPOKES['bronx']['name']='Bronx'
PARENT_NAME={'nyc':'NYC','long-island':'Long Island','hudson-valley':'Hudson Valley'}
GBP = {
 'brooklyn': dict(street='1282 Troy Ave', city='Brooklyn', zip='11203', review='https://g.page/r/CeOVMclhop84EBM/review'),
 'bronx': dict(street='460 E Fordham Rd', city='Bronx', zip='10458', review='https://g.page/r/Ca_eMyn6_brDEBM/review'),
}

def m(x): return '$%.2f' % x
def H(s): return s  # strings already HTML-safe from drafts

def tbl(head, rows):
    th = ''.join('<th style="text-align:left;padding:12px;background:var(--d);color:#fff">%s</th>' % h for h in head)
    tr = ''.join('<tr>' + ''.join('<td style="padding:10px 12px;border-bottom:1px solid var(--b)%s">%s</td>'
                 % (';font-weight:700;white-space:nowrap' if i == len(r) - 1 else '', c) for i, c in enumerate(r)) + '</tr>' for r in rows)
    return ('<div class="rv" style="transition-delay:.14s;overflow-x:auto"><table style="width:100%;max-width:820px;border-collapse:collapse;'
            'background:#fff;border:1px solid var(--b);border-radius:12px;overflow:hidden;margin:12px 0 26px;font-size:.95rem;color:var(--d)">'
            '<tr>' + th + '</tr>' + tr + '</table></div>')

def h3p(q, a, d=.12):
    return ('<div class="rv" style="transition-delay:%ss;margin-bottom:22px"><h3 style="font-size:1.12rem;font-weight:800;margin-bottom:8px">%s</h3>'
            '<p class="bt">%s</p></div>' % (d, q, a))

def lcards(items):
    return ('<div class="rv" style="transition-delay:.14s;display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px">' +
            ''.join('<div class="lcard"><div style="font-size:1.4rem">&#x1F4CD;</div><div><div class="lname">%s</div><div class="ldet">%s</div></div></div>'
                    % (i['name'], i['text']) for i in items) + '</div>')

def process(steps):
    return ('<div class="pg rv" style="transition-delay:.14s">' +
            ''.join('<div class="pc" style="position:relative"><div class="pn">%d</div><div class="pt">%s</div><div class="pd">%s</div></div>'
                    % (i + 1, s['title'], s['text']) for i, s in enumerate(steps)) + '</div>')

def full_form(k, area):
    return ('<div class="rv" style="transition-delay:.12s;max-width:720px"><form action="https://api.web3forms.com/submit" method="POST" '
            'style="display:grid;gap:10px;background:#fff;border:1px solid var(--b);border-radius:14px;padding:24px">'
            '<input type="hidden" name="access_key" value="88890030-1770-483e-a622-0e054d8e14b1">'
            '<input type="hidden" name="subject" value="New TV Mounting Quote Request &mdash; %s">'
            '<input type="hidden" name="from_name" value="Abstract Enterprises Website">'
            '<input type="hidden" name="redirect" value="https://www.abstractenterprisessecuritysystems.com/tv-mounting-prices-%s">'
            '<input type="checkbox" name="botcheck" style="display:none">'
            '<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px"><input name="name" required placeholder="Full Name *" style="padding:12px;border:1px solid var(--b);border-radius:8px">'
            '<input name="phone" type="tel" required placeholder="Phone *" style="padding:12px;border:1px solid var(--b);border-radius:8px"></div>'
            '<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px"><input name="email" type="email" placeholder="Email" style="padding:12px;border:1px solid var(--b);border-radius:8px">'
            '<select name="service" required style="padding:12px;border:1px solid var(--b);border-radius:8px"><option value="" disabled selected>What do you need? *</option>'
            '<option>One TV</option><option>Two or more TVs</option><option>TV above a fireplace</option><option>Hidden wires</option>'
            '<option>Soundbar / home theater</option><option>Commercial / business TVs</option><option>Move or remount a TV</option></select></div>'
            '<textarea name="message" rows="4" placeholder="TV size, wall type (drywall, plaster, brick, concrete), town, and anything else we should know" style="padding:12px;border:1px solid var(--b);border-radius:8px"></textarea>'
            '<label style="display:flex;gap:8px;font-size:.75rem;color:#6b7280;line-height:1.5"><input type="checkbox" name="sms_consent" value="yes" required style="margin-top:3px">'
            'I agree to receive texts and calls from Abstract Enterprises about my request. Msg &amp; data rates may apply. Reply STOP to opt out. '
            '<a href="/sms-consent" style="color:var(--a)">SMS Consent</a></label>'
            '<button type="submit" class="bp" style="border:0;cursor:pointer">Request My Quote &rarr;</button></form></div>') % (area, k)

def build(k):
    A = HUBS.get(k) or SPOKES[k]; PAR = A.get('parent'); PK = 150 if k == 'manhattan' else 0; D = json.load(open(os.path.join(BP, k + '.json')))
    P = A['place']; base = A['base']; hourly = A['hourly']; g = GBP[A['gbp']]
    svc = '/' + A['svc']; slug = 'tv-mounting-prices-' + k
    s = T

    # ---- head (elements 1-3)
    s = re.sub(r'<title>[^<]*</title>', '<title>%s</title>' % D['title'].replace('&', '&amp;').replace('&amp;amp;', '&amp;'), s, 1)
    s = re.sub(r'<link rel="canonical" href="[^"]*"', '<link rel="canonical" href="%s/%s"' % (BASE, slug), s, 1)
    s = re.sub(r'<meta name="description" content="[^"]*"', '<meta name="description" content="%s"' % html.escape(D['meta'], quote=True), s, 1)
    s = re.sub(r'<meta name="keywords" content="[^"]*"', '<meta name="keywords" content="%s"' % html.escape(', '.join(D['keywords_used'][:25]), quote=True), s, 1)
    s = re.sub(r'<meta name="robots" content="[^"]*">', '', s)
    s = s.replace('<meta charset="UTF-8">', '<meta charset="UTF-8"><meta name="robots" content="index, follow">', 1)
    for prop, val in (("og:title", D['title']), ("og:description", D['meta']), ("og:url", "%s/%s" % (BASE, slug))):
        s = re.sub(r'(<meta property="%s" content=")[^"]*"' % prop, r'\g<1>%s"' % html.escape(val, quote=True), s)

    # ---- schema stack (LocalBusiness per GBP routing, FAQPage = §17, + Service, HowTo, Person, Breadcrumb)
    lb = {"@context": "https://schema.org", "@type": "LocalBusiness", "@id": BASE + "/#" + A['gbp'],
          "name": "Abstract Enterprises Security Systems", "telephone": "(800) 486-0943", "url": "%s/%s" % (BASE, slug),
          "image": BASE + "/images/logo.png", "priceRange": "$$",
          "address": {"@type": "PostalAddress", "streetAddress": g['street'], "addressLocality": g['city'], "addressRegion": "NY",
                      "postalCode": g['zip'], "addressCountry": "US"},
          "areaServed": strip(P), "openingHours": "Mo-Su 08:00-20:00", "hasCredential": "NYS Low-Voltage License #12000287431",
          "description": strip(D['meta']), "dateModified": TODAY}
    fq = {"@context": "https://schema.org", "@type": "FAQPage",
          "mainEntity": [{"@type": "Question", "name": strip(x['q']), "acceptedAnswer": {"@type": "Answer", "text": strip(x['a'])}} for x in D['faq']]}
    blocks = list(re.finditer(r'<script type="application/ld\+json">.*?</script>', s, re.S))[:2]
    new = ['<script type="application/ld+json">\n%s\n</script>' % json.dumps(lb, ensure_ascii=False),
           '<script type="application/ld+json">\n%s\n</script>' % json.dumps(fq, ensure_ascii=False)]
    for b, n in reversed(list(zip(blocks, new))):
        s = s[:b.start()] + n + s[b.end():]
    extra = [
     {"@context": "https://schema.org", "@type": "Service", "serviceType": "TV mounting", "name": "TV Mounting in " + strip(P),
      "areaServed": strip(P), "provider": {"@id": BASE + "/#" + A['gbp']},
      "offers": {"@type": "Offer", "priceCurrency": "USD", "price": "%.2f" % base,
                 "description": "32-55 inch TV, flat or tilt mount on drywall over wood studs, labor included" + ("; plus flat $150 Manhattan parking charge" if PK else "")}},
     {"@context": "https://schema.org", "@type": "HowTo", "name": "How to book TV mounting in " + strip(P),
      "step": [{"@type": "HowToStep", "position": i + 1, "name": strip(x['title']), "text": strip(x['text'])} for i, x in enumerate(D['process'])]},
     {"@context": "https://schema.org", "@type": "Person", "name": "Anwar Timothy", "jobTitle": "Owner",
      "worksFor": {"@type": "Organization", "name": "Abstract Enterprises Security Systems, Inc."},
      "hasCredential": {"@type": "EducationalOccupationalCredential", "credentialCategory": "license", "name": "NYS Low-Voltage License #12000287431"}},
     {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
      {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE + "/"},
      ] + ([{"@type": "ListItem", "position": 2, "name": "TV Mounting Prices " + PARENT_NAME[PAR], "item": "%s/tv-mounting-prices-%s" % (BASE, PAR)}] if PAR else []) + [
      {"@type": "ListItem", "position": 3 if PAR else 2, "name": "TV Mounting Prices " + A['name'], "item": "%s/%s" % (BASE, slug)}]},
     {"@context": "https://schema.org", "@type": "WebPage", "name": strip(D['title']), "url": "%s/%s" % (BASE, slug),
      "dateModified": TODAY, "author": {"@type": "Person", "name": "Anwar Timothy"}}]
    extra_schema = ''.join('<script type="application/ld+json">%s</script>\n' % json.dumps(x, ensure_ascii=False) for x in extra)

    # ---- hero (element 4)
    s = re.sub(r'(<div class="hbadge">.*?</svg>).*?(</div></div>)', r'\g<1> %s\g<2>' % D['hero_badge'].upper(), s, 1, re.S)
    s = re.sub(r'<h1>.*?</h1>', '<h1>TV Mounting<br>Prices in<br><span class="ac">%s</span></h1>' % P, s, 1, re.S)
    s = re.sub(r'(<p style="font-size:\.85rem;font-weight:600;letter-spacing:\.06em[^>]*>).*?(</p>)',
               r'\g<1>Updated October 2026 &middot; Flat Published Prices &middot; Licensed &amp; Insured\g<2>', s, 1, re.S)
    s = re.sub(r'<p class="hsub">.*?</p>', lambda _: '<p class="hsub">%s</p>' % D['hero_sub'], s, 1, re.S)
    s = re.sub(r'(<div class="rv br"[^>]*>)<a href="/free-quote" class="bp">[^<]*</a>', r'\g<1><a href="/free-quote" class="bp">Get Free Quote &rarr;</a>', s, 1)
    s = re.sub(r'(<div class="hf-title" style="font-size:1rem">).*?(</div>)', r'\g<1>Get a TV Mounting Quote\g<2>', s, 1)
    s = re.sub(r'(<input type="hidden" name="subject" value=")[^"]*"', r'\g<1>New TV Mounting Lead &mdash; %s"' % A['name'], s, 1)
    opts = '<option value="" disabled selected>Service *</option>' + ''.join('<option value="%s">%s</option>' % (o, o) for o in
            ['One TV', 'Two or More TVs', 'Above the Fireplace', 'Hidden Wires', 'Soundbar / Home Theater', 'Commercial / Business', 'Move or Remount'])
    s = re.sub(r'(<select name="service" required[^>]*>).*?(</select>)', r'\g<1>%s\g<2>' % opts, s, 1, re.S)
    stats = ('<div class="stats rv" style="transition-delay:.3s"><div class="st"><div class="stn">25+</div><div class="stl">Years Experience</div></div>'
             '<div class="st"><div class="stn">&#x2713;</div><div class="stl">Same-Day Estimates</div></div>'
             '<div class="st"><div class="stn">100%</div><div class="stl">Licensed &amp; Insured</div></div>'
             '<div class="st"><div class="stn">$0</div><div class="stl">Monthly Fees</div></div></div>')
    s, nst = re.subn(r'<div class="stats rv"[^>]*>(?:<div class="st"><div class="stn">[^<]*</div><div class="stl">[^<]*</div></div>){4}</div>', stats, s, count=1)
    assert nst == 1, 'stats bar not replaced'

    # ---- body
    qa_box = ('<div class="rv" style="transition-delay:.1s"><div style="background:#fff;border:1px solid var(--b);border-left:4px solid var(--a);'
              'border-radius:12px;padding:20px 22px;margin:4px 0 24px;max-width:840px;color:var(--d);line-height:1.7"><b>Quick answer:</b> %s</div></div>' % D['quick_answer'])
    facts = ('<div class="rv" style="transition-delay:.18s"><ul style="margin:8px 0 0 20px;line-height:1.9;color:var(--g)">' +
             ''.join('<li>%s <a class="lnk" href="%s" rel="nofollow noopener" target="_blank" style="font-size:.8rem">(source)</a></li>'
                     % (f['text'], html.escape(f['source'], quote=True)) for f in D['why_facts']) + '</ul></div>')
    b = []
    b.append('<!-- ELEMENT 5: THE NEIGHBORHOOD + 5.5 LOCAL FACTS -->\n' + sec('sw', 'The Neighborhood', D['why_h2'], '',
             qa_box + ''.join(p(x, .12 + i * .02) for i, x in enumerate(D['why_paras'])) + facts))
    cov = ''.join(h3p(x['h3'], x['text'], .12) for x in D.get('coverage_sections', []))
    b.append('<!-- ELEMENT 6: WHAT WE INSTALL -->\n' + sec('sg', 'What We Install', D['services_h2'], '', cards([(c['icon'], c['title'], c['text']) for c in D['services']]) + ('<div style="margin-top:34px"></div>' + cov if cov else '')))
    b.append('<!-- ELEMENT 7 + 7.5: BUILDING SPECIALISTS -->\n' + sec('sw', 'Building Specialists', D['buildings_h2'], '',
             cards([(c['icon'], c['title'], c['text']) for c in D['buildings']]) +
             '<div style="margin-top:30px"></div>' + ''.join(h3p(x['title'], x['text'], .14) for x in D['building_methods'])))
    b.append('<!-- ELEMENT 8 + 8.5: COMMERCIAL -->\n' + sec('sg', 'Commercial TV Mounting', D['commercial_h2'], '',
             p(D['commercial_intro']) + lcards(D['corridors']) + '<div style="margin-top:28px"></div>' +
             ''.join(h3p(x['title'], x['text'], .16) for x in D['compliance'])))
    b.append('<!-- ELEMENT 9: YOUR QUESTIONS ANSWERED -->\n' + sec('sw', 'Your Questions Answered', D['qa_h2'], '',
             ''.join(h3p(x['q'], x['a'], .1) for x in D['qa'])))
    c = D['comparison']
    b.append('<!-- ELEMENT 10 + 24: EQUIPMENT + COMPARISON -->\n' + sec('sg', 'Equipment', D['equipment_h2'], '',
             cards([(x['icon'], x['title'], x['text']) for x in D['equipment']]) +
             '<div class="rv" style="margin-top:34px"><h3 style="font-size:1.25rem;font-weight:800">%s</h3></div>' % c['title'] + tbl(c['head'], c['rows'])))
    b.append('<!-- ELEMENT 29: MID-PAGE CTA -->\n<section class="sd" style="padding:60px 0;text-align:center"><div class="cx">'
             '<div class="rv"><h2 style="color:#fff">See Your Exact Price in <span style="color:var(--a)">About a Minute</span></h2></div>'
             '<div class="rv" style="transition-delay:.08s"><p style="color:rgba(255,255,255,.6);max-width:620px;margin:0 auto 26px">Pick your TV size, mount and wall in the calculator, then book a 2-hour window and pay online.</p></div>'
             '<div class="rv br" style="justify-content:center"><a href="#aessTvCalc" class="bp">Open the Price Calculator &rarr;</a>'
             '<a href="tel:8004860943" class="bo" style="color:#fff;border-color:#fff">Call (800) 486-0943</a></div></div></section>\n')
    b.append('<!-- ELEMENT 10.5: AI OVERVIEW REALITY CHECK -->\n' + sec('sw', 'AI Overview Reality Check', D['ai_h2'], '',
             p(D['ai_intro']) + ''.join('<div class="rv" style="transition-delay:.12s;margin:26px 0 8px"><h3 style="font-size:1.12rem;font-weight:800">%d. AI says: &ldquo;%s&rdquo;</h3></div>'
                                       % (i + 1, x['claim'].strip().strip('“”"')) + ''.join(p(pp, .14) for pp in x['paras']) for i, x in enumerate(D['ai_items']))))
    b.append('<!-- ELEMENT 11: GET IN TOUCH -->\n' + sec('sg', 'Get in Touch', 'Request a Free', 'TV Mounting Quote',
             p('Several TVs, a commercial job, or a wall you&#x2019;re not sure about? Send the details and we&#x2019;ll reply with a written quote.') + full_form(k, A['name'])))
    b.append('<!-- ELEMENT 12: HOW IT WORKS -->\n' + sec('sd', 'How It Works', 'Our TV Mounting', 'Process', process(D['process']), dark=True))
    b.append('<!-- ELEMENT 21: FIELD NOTES -->\n' + sec('sw', 'Field Notes', 'From the', 'Truck', p(D['field_notes'])))
    b.append('<!-- ELEMENT 13: COVERAGE AREA -->\n' + sec('sg', 'Coverage Area', D['landmarks_h2'], '', lcards(D['landmarks']) + p(D['also_serve'], .18)))

    # §14 pricing (verified numbers only)
    if PAR:
        rows=[]
        for wn, wa in (('Drywall over wood studs',0),('Drywall over metal studs',30),('Plaster',45),('Brick or stone',65),('Concrete or cinder block',75)):
            rows.append((wn,)+tuple(m(base+sa+wa+PK) for sa in (0,30,60,100)))
        nbt = ('<div class="rv"><h3 style="font-size:1.15rem;font-weight:800;margin-top:14px">Neighborhood by neighborhood: what a 65&Prime; job usually costs in %s</h3></div>' % A['areas'][0][0] +
               tbl(['Neighborhood', 'Housing you&#x2019;ll mostly find', 'Walls we plan for', 'Typical 65&Prime; flat/tilt job%s' % (' (with parking)' if PK else '')], NB(k, base, PK)) +
               p('Every building is different, so we confirm the wall when we arrive and the calculator below gives your exact number.', .14)) if k in ('brooklyn','queens','manhattan','bronx','nassau-county','suffolk-county','westchester-county','rockland-county','orange-county','putnam-county','dutchess-county','ulster-county') else ''
        if k in ROOMS:
            rt, rrows, rnote = ROOMS[k](base)
            nbt += ('<div class="rv"><h3 style="font-size:1.15rem;font-weight:800;margin-top:14px">%s</h3></div>' % rt +
                    tbl(['Room', 'Typical setup', 'Labor'], rrows) + p(rnote, .14))
        if k in LOGI:
            lt, lrows, lnote = LOGI[k]
            nbt += ('<div class="rv"><h3 style="font-size:1.15rem;font-weight:800;margin-top:14px">%s</h3></div>' % lt +
                    tbl(['What the building or job needs', 'How we handle it', 'Cost to you'], lrows) + p(lnote, .14))
        if k == 'manhattan':
            nbt += ('<div class="rv"><h3 style="font-size:1.15rem;font-weight:800;margin-top:14px">Manhattan building logistics and what they cost you</h3></div>' +
                tbl(['What the building or job needs', 'How we handle it', 'Cost to you'], [
                    ('Certificate of insurance naming the building and management company', 'Sent to the managing agent before the visit, matched to their sample wording', 'Free'),
                    ('Service or freight elevator reservation', 'You or your doorman book the slot; we arrive inside it', '$0 from us'),
                    ('Work allowed only on weekdays during set hours', 'We book inside the building&#x2019;s window', '$0'),
                    ('Street parking for the work van', 'Flat charge on every Manhattan job, no meter math on your bill', '$150'),
                    ('Walk-up, 3rd floor or higher, no elevator', 'Two trips with tools and the TV', '$40'),
                    ('Metal-stud partition and a TV over about 65 lb', 'Plywood backer board behind the bracket, painted to match on request', '$85 + $30 metal-stud add'),
                    ('Concrete or block wall in a postwar or new tower', 'Hammer-drill with masonry anchors rated for the TV and bracket', '+$75'),
                    ('Wires hidden in the wall', 'Code-compliant power and cable kit; no new outlet wiring', '$169'),
                    ('Old TV left behind after the install', 'Taken down and hauled away so it doesn&#x2019;t sit in the hallway', '$85 + $79')]) +
                p('Need the alteration agreement or board paperwork filled out? Send it with your request and we&#x2019;ll return it with the COI.', .14))
        hubtbl=('<div class="rv"><h3 style="font-size:1.15rem;font-weight:800;margin-top:10px">%s prices by wall and TV size%s</h3></div>' % (A['areas'][0][0], ' (parking included)' if PK else '') +
                tbl(['Wall', 'Up to 55&Prime;', '56&ndash;65&Prime;', '66&ndash;75&Prime;', '76&ndash;85&Prime;'], rows) +
                (p('Every Manhattan job carries a flat $150 parking charge, already added to every number in this table. The size, wall, mount and extras tables below show the labor before parking.', .14) if PK else '') +
                nbt + p('Flat or tilt mount, labor only, bracket extra. Back up to the <a class="lnk" href="/tv-mounting-prices-%s">TV mounting prices for all of %s</a>.' % (PAR, PARENT_NAME[PAR]), .15))
    else:
        MAT = {'nyc': [('Brooklyn',179.99),('Queens',179.99),('The Bronx',209.99),('Staten Island',209.99),('Manhattan*',244.99)],
               'long-island': [('Nassau County',209.99),('Suffolk County',229.99)],
               'hudson-valley': [('Westchester',219.99),('Rockland',219.99),('Orange County',229.99),('Putnam',229.99),('Dutchess',254.99),('Ulster',254.99)]}[k]
        hubtbl = (tbl(['Area', 'Up to 55&Prime;', '65&Prime;', '75&Prime;', '85&Prime;', '65&Prime; over a brick fireplace'],
                      [(n, m(v), m(v+30), m(v+60), m(v+100), m(v+30+130+65)) for n, v in MAT]) +
                  (p('*Manhattan adds a flat $150 parking charge to every job.', .14) if k == 'nyc' else '') +
                  (('<div class="rv"><h3 style="font-size:1.15rem;font-weight:800;margin-top:14px">What usually changes the price, borough by borough</h3></div>' +
                    tbl(['Borough', 'Walls we see most', 'Common add-ons', 'Typical extra'],
                        [('Brooklyn', 'Plaster over brick in brownstones and row houses; exposed brick', 'Plaster or brick charge, cord cover on brick, walk-up carry', '+$45 to +$65, $59, $40'),
                         ('Queens', 'Plaster in prewar co-ops; drywall over wood studs in two-families and houses', 'Fireplace mounts in detached houses, cable runs to basements', '+$130, $99'),
                         ('The Bronx', 'Thick prewar plaster; concrete and block in large co-op complexes', 'Plaster or concrete charge, COI for the building', '+$45 to +$75, COI free'),
                         ('Staten Island', 'Drywall over wood studs in houses; brick and stone fireplaces', 'Above-fireplace mounts, outdoor patio TVs', '+$130, +$90'),
                         ('Manhattan', 'Concrete and metal-stud partitions in high-rises; plaster in prewar co-ops', 'Parking, metal studs or concrete, backer board for big TVs', '$150, +$30 to +$75, $85')])) if k == 'nyc' else '') +
                  p('All prices: flat or tilt mount on drywall over wood studs unless noted, labor only, bracket extra.', .15))
    sizes = tbl(['TV size', 'Price in %s' % A['areas'][0][0]], [
        ('32&Prime;&ndash;55&Prime;', m(base)), ('56&Prime;&ndash;65&Prime;', m(base + 30)), ('66&Prime;&ndash;75&Prime;', m(base + 60)),
        ('76&Prime;&ndash;85&Prime;', m(base + 100)), ('86&Prime;&ndash;97&Prime; (two technicians)', m(base + 175)), ('98&Prime; and up (two technicians)', m(base + 220))])
    walls = tbl(['Wall', 'Added'], [('Drywall over wood studs', '$0'), ('Drywall over metal studs', '+$30'), ('Plaster', '+$45'),
        ('Brick or stone', '+$65'), ('Concrete or cinder block', '+$75'), ('Tile or marble', '+$95')])
    mounts = tbl(['Mount', 'Added'], [('Flat or tilting', '$0'), ('Full-motion', '+$40'), ('Corner', '+$40'), ('Samsung Frame / art TV', '+$70'),
        ('Ceiling', '+$85'), ('Outdoor (patio / deck)', '+$90'), ('Above the fireplace', '+$130'), ('Pull-down fireplace', '+$160')])
    extras = tbl(['Extra', 'Price'], [('In-wall wire concealment (code-compliant power &amp; cable kit)', '$169'), ('Paintable cord cover', '$59'),
        ('Cable run to a cabinet or other spot (up to 25 ft)', '$99'), ('Soundbar placed / wall-mounted', '$79 / $129'),
        ('Streaming device or game console setup', '$49 each'), ('A/V receiver &amp; speakers', '$129'), ('Sonos / wireless surround', '$125'),
        ('Universal remote programming', '$99'), ('Full home theater setup', '$350'), ('Take down old TV / remove old bracket', '$85 / $45'),
        ('Plywood backer board', '$85'), ('High mount (above ~8 ft)', '$75'), ('Walk-up, 3rd floor+, no elevator', '$40'),
        ('Haul away old TV / remove boxes', '$79 / $25'), ('Certificate of insurance (COI)', 'Free'),] + ([('Manhattan parking (every job)', '$150')] if PK else []) + [
        ('Setup-only visit (smart TV, WiFi, cable box)', 'First hour %s, then 30-min blocks' % m(hourly))])
    calc = ('<div class="rv" style="transition-delay:.12s"><div id="aessTvCalc" data-area="%s" data-label="%s"></div></div>'
            '<script src="/js/tv-calc.js?v=8"></script>' % (A['zone'], strip(P)))
    b.append('<!-- ELEMENT 14: PRICING -->\n' + sec('sw', 'Pricing', 'TV Mounting Cost in', P,
             p(D['pricing_intro']) + hubtbl + p('Size prices below are for %s; other areas add the same difference on every line, and the calculator does it for you.' % A['areas'][0][0], .14)
             + '<div class="rv"><h3 style="font-size:1.15rem;font-weight:800;margin-top:10px">By TV size</h3></div>' + sizes
             + '<div class="rv"><h3 style="font-size:1.15rem;font-weight:800">By wall</h3></div>' + walls
             + '<div class="rv"><h3 style="font-size:1.15rem;font-weight:800">By mount</h3></div>' + mounts
             + '<div class="rv"><h3 style="font-size:1.15rem;font-weight:800">Extras</h3></div>' + extras
             + '<div class="rv"><h3 style="font-size:1.15rem;font-weight:800">Your exact price</h3></div>' + calc))
    std = base + 30 + 40 + 169; prem = base + 60 + 130 + 65 + 169 + 129
    pk = [('STARTER', m(base), 'Up to 55&Prime; &middot; flat or tilt mount &middot; drywall &middot; connected to power + 2 devices &middot; cables tidied', D['package_notes']['starter']),
          ('STANDARD', m(std), '56&Prime;&ndash;65&Prime; &middot; full-motion mount &middot; drywall &middot; wires hidden in the wall (power &amp; cable kit included)', D['package_notes']['standard']),
          ('PREMIUM', m(prem), '66&Prime;&ndash;75&Prime; &middot; above a brick or stone fireplace &middot; wires hidden in the wall &middot; soundbar wall-mounted &amp; connected', D['package_notes']['premium'])]
    pkh = ('<div class="prg rv" style="transition-delay:.14s">' + ''.join(
        '<div class="prc lt"><div class="prl">%s</div><div class="pra" style="color:var(--d)">%s</div><div class="prd" style="color:var(--g)">%s</div>'
        '<div class="prd" style="color:var(--d);margin-top:10px;font-weight:600">%s</div></div>' % x for x in pk) + '</div>')
    b.append('<!-- ELEMENT 15 + 15.5: PACKAGES + BYOE -->\n' + sec('sd', 'Shop Our Packages', 'TV Mounting', 'Packages &amp; Pricing',
             '<div class="rv"><p style="color:rgba(255,255,255,.6);max-width:720px;margin-bottom:26px">%s Package prices are for %s; brackets are extra%s.</p></div>' % (D['packages_intro'], A['areas'][0][0], ', and the flat $150 Manhattan parking charge is added to each' if PK else '')
             + pkh + '<div class="rv" style="margin-top:26px"><p style="color:rgba(255,255,255,.75);max-width:760px"><b>Bring your own:</b> %s</p></div>' % D['byoe'], dark=True))
    services = [('/security-camera-installation-nyc', 'Security Cameras'), ('/intercom-installation-nyc', 'Intercoms'), ('/access-control-installation-nyc', 'Access Control'),
                ('/alarm-installation-nyc', 'Alarm Systems'), ('/structured-cabling-installation-nyc', 'Structured Cabling'), ('/network-installation-nyc', 'WiFi &amp; Networks'),
                ('/av-sound-installation-nyc', 'AV &amp; Sound'), ('/video-wall-installation-nyc', 'Video Walls'), (svc, 'TV Mounting &amp; Installation Service')]
    b.append('<!-- ELEMENT 16: COMPLETE SERVICES -->\n' + sec('sd', 'Complete Services', 'Everything Else We Install in', P,
             '<div class="pg rv" style="transition-delay:.14s">' + ''.join('<a href="%s" class="pc" style="text-decoration:none"><div class="pt">%s &rarr;</div></a>' % x for x in services) + '</div>', dark=True))
    b.append('<!-- ELEMENT 17: FAQ (schema = ELEMENT 18 in head) -->\n' + sec('sg', 'FAQ', 'TV Mounting Prices', 'FAQ', faq([(x['q'], x['a']) for x in D['faq']])))
    kids = A['kids']
    LOC = {
     'nyc': [('/tv-mounting-prices-manhattan','TV mounting Manhattan'),('/tv-installation-brooklyn','TV installation Brooklyn'),('/tv-mounting-prices-queens','TV wall mounting Queens'),
             ('/tv-mounting-prices-bronx','TV mounting Bronx'),('/tv-installation-staten-island','TV installation Staten Island'),('/tv-mounting-prices-queens','TV mounting Astoria Queens'),
             ('/tv-mounting-prices-brooklyn','TV mounting Williamsburg Brooklyn')],
     'long-island': [('/tv-installation-nassau-county','TV installation Nassau County'),('/tv-mounting-prices-suffolk-county','TV mounting Suffolk County'),
             ('/tv-mounting-prices-nassau-county','TV installation Hempstead'),('/tv-mounting-prices-nassau-county','TV mounting Hicksville'),
             ('/tv-mounting-prices-suffolk-county','TV mounting Huntington'),('/tv-mounting-prices-suffolk-county','TV mounting Islip'),('/tv-mounting-prices-suffolk-county','TV installation Babylon')],
     'hudson-valley': [('/tv-mounting-prices-westchester-county','TV mounting Westchester County'),('/tv-mounting-prices-rockland-county','TV mounting Rockland County'),
             ('/tv-installation-orange-county','TV installation Orange County'),('/tv-mounting-prices-putnam-county','TV mounting Putnam County'),
             ('/tv-installation-dutchess-county','TV installation Dutchess County'),('/tv-mounting-prices-ulster-county','TV mounting Ulster County'),
             ('/tv-installation-westchester-county','TV installation Yonkers'),('/tv-mounting-prices-westchester-county','TV mounting White Plains'),
             ('/tv-installation-rockland-county','TV installation New City')],
     'manhattan': [('/tv-mounting-prices-nyc','TV mounting NYC'),('/tv-mounting-prices-brooklyn','TV mounting Williamsburg Brooklyn'),('/tv-mounting-prices-queens','TV mounting Astoria Queens')],
     'brooklyn': [('/tv-mounting-prices-nyc','TV mounting NYC'),('/tv-mounting-prices-manhattan','TV mounting Manhattan'),('/tv-mounting-prices-queens','TV wall mounting Queens')],
     'bronx': [('/tv-mounting-prices-nyc','TV mounting NYC'),('/tv-mounting-prices-manhattan','TV mounting Manhattan'),('/tv-mounting-prices-queens','TV wall mounting Queens')],
     'staten-island': [('/tv-mounting-prices-nyc','TV mounting NYC'),('/tv-mounting-prices-brooklyn','TV mounting Williamsburg Brooklyn'),('/tv-mounting-prices-bronx','TV mounting Bronx')],
     'nassau-county': [('/tv-mounting-prices-long-island','TV mounting Long Island'),('/tv-mounting-prices-suffolk-county','TV mounting Suffolk County')],
     'suffolk-county': [('/tv-mounting-prices-long-island','TV mounting Long Island'),('/tv-mounting-prices-nassau-county','TV mounting prices Nassau County')],
     'westchester-county': [('/tv-mounting-prices-hudson-valley','TV mounting in the Hudson Valley'),('/tv-mounting-prices-rockland-county','TV mounting Rockland County')],
     'rockland-county': [('/tv-mounting-prices-hudson-valley','TV mounting in the Hudson Valley'),('/tv-mounting-prices-westchester-county','TV mounting Westchester County')],
     'orange-county': [('/tv-mounting-prices-hudson-valley','TV mounting in the Hudson Valley'),('/tv-mounting-prices-rockland-county','TV mounting Rockland County'),('/tv-mounting-prices-putnam-county','TV mounting Putnam County')],
     'putnam-county': [('/tv-mounting-prices-hudson-valley','TV mounting in the Hudson Valley'),('/tv-mounting-prices-westchester-county','TV mounting Westchester County'),('/tv-mounting-prices-dutchess-county','TV mounting prices Dutchess County')],
     'dutchess-county': [('/tv-mounting-prices-hudson-valley','TV mounting in the Hudson Valley'),('/tv-mounting-prices-putnam-county','TV mounting Putnam County'),('/tv-mounting-prices-ulster-county','TV mounting Ulster County')],
     'ulster-county': [('/tv-mounting-prices-hudson-valley','TV mounting in the Hudson Valley'),('/tv-mounting-prices-dutchess-county','TV mounting prices Dutchess County'),('/tv-mounting-prices-orange-county','TV mounting prices Orange County NY')],
     'queens': [('/tv-mounting-prices-nyc','TV mounting NYC'),('/tv-mounting-prices-manhattan','TV mounting Manhattan'),('/tv-mounting-prices-brooklyn','TV mounting Williamsburg Brooklyn')],
    }.get(k, [('/tv-mounting-prices-%s' % PAR, 'TV mounting %s' % PARENT_NAME.get(PAR, ''))])
    selfterm = {'nyc':'TV mounting NYC','long-island':'TV mounting Long Island','hudson-valley':'TV mounting in the Hudson Valley','manhattan':'TV mounting Manhattan','brooklyn':'TV mounting prices Brooklyn','queens':'TV mounting prices Queens NY','bronx':'TV mounting Bronx','nassau-county':'TV mounting Hicksville &amp; Hempstead','suffolk-county':'TV mounting Huntington, Islip &amp; Babylon','westchester-county':'TV mounting White Plains','rockland-county':'TV mounting prices Rockland County','orange-county':'TV mounting prices Orange County NY','putnam-county':'TV mounting Putnam County','dutchess-county':'TV mounting prices Dutchess County','ulster-county':'TV mounting Ulster County'}.get(k, 'TV mounting prices ' + A['name'])
    up = p('<b>Up one level:</b> <a class="lnk" href="/tv-mounting-prices-%s">TV mounting prices across %s</a>' % (PAR, PARENT_NAME[PAR]), .12) if PAR else ''
    silo = up + (p('<b>%s:</b> ' % A['kids_title'] + ' &middot; '.join('<a class="lnk" href="/tv-mounting-prices-%s">TV mounting prices %s</a>' % (kk, nm) for kk, nm, _ in kids)) +
            p('<b>Book the service:</b> <a class="lnk" href="%s">TV mounting and installation service in %s</a>%s' % (svc, P, '' if PAR else ' &middot; ') +
              ('' if PAR else ' &middot; '.join('<a class="lnk" href="/%s">TV installation %s</a>' % (sv, nm) for _, nm, sv in kids)) +
              ' &middot; <a class="lnk" href="/tv-installation-policies">TV installation policies</a>', .14) +
            p('<b>Popular searches we cover:</b> %s &middot; ' % selfterm + ' &middot; '.join('<a class="lnk" href="%s">%s</a>' % x for x in LOC), .16))
    b.append('<!-- ELEMENT 19: ALL AREAS SERVED (silo) -->\n' + sec('sw', 'All Areas Served', A['kids_title'], '', silo))
    b.append('<!-- ELEMENT 18 (blueprint 20-elem order): LOCAL PROBLEMS / SUMMARY -->\n' + sec('sg', 'The Short Version', D['local_close_h2'], '', p(D['local_close'])))
    b.append('<!-- CTA to /free-quote -->\n<section class="sw" style="text-align:center;padding:80px 0"><div class="cx">'
             '<div class="rv"><h2>Get Your TV Mounted in %s <span class="ac">This Week</span></h2></div>'
             '<div class="rv" style="transition-delay:.08s"><p class="bt" style="max-width:640px;margin:0 auto 30px">Published prices, 2-hour arrival windows, '
             'licensed and insured technicians. Book online or ask for a written quote.</p></div><div class="rv br" style="transition-delay:.14s;justify-content:center">'
             '<a href="/free-quote" class="bp">Get Your Free Quote &rarr;</a><a href="tel:8004860943" class="bo">Call (800) 486-0943</a></div>'
             '<div class="rv" style="margin-top:22px"><p class="bt" style="font-size:.85rem">Updated October 13, 2026 &middot; Written by Anwar Timothy, owner, NYS Low-Voltage License #12000287431 &middot; '
             '<a class="lnk" href="%s" target="_blank" rel="noopener">Read our Google reviews</a></p></div></div></section>\n' % (P, g['review']))
    body = extra_schema + '\n'.join(b)
    a = s.index('<!-- ELEMENT 3: INTRO -->'); e = s.index('<footer')
    s = s[:a] + body + s[e:]
    # ---- element 20 footer NAP per GBP routing
    nap = ('Abstract Enterprises Security Systems, Inc. &middot; %s, %s, NY %s &middot; <a href="tel:8004860943" style="color:rgba(255,255,255,.5)">(800) 486-0943</a> &middot; NYS Lic. #12000287431'
           % (g['street'], g['city'], g['zip']))
    s = re.sub(r'(<div class="fts">)[^<]*(</div>)', r'\g<1>TV MOUNTING &middot; %s\g<2>' % strip(P).upper(), s, 1)
    s = re.sub(r'(<div class="ftc">)', r'\g<1>%s<br>' % nap, s, 1)
    s = re.sub(r'&middot; Alarm Installation New York City', '&middot; TV Mounting Prices %s' % A['name'], s)
    # remove template's pay-service CTA block (alarm/buzzer) — TV pays via calculator
    i = s.find('<!-- PAY SERVICE CALL CTA -->')
    if i >= 0:
        j = s.index('<div class="sticky-pricing-bar"', i); s = s[:i] + s[j:]
    open(os.path.join(SITE, slug + '.html'), 'w', encoding='utf-8').write(s)
    return slug

if __name__ == '__main__':
    for k in sys.argv[1:] or HUBS:
        print(build(k))
