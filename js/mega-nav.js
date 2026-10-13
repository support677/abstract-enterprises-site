/* MEGA-NAV v2.0 — Desktop hover + Mobile stepped funnel */
(function(){
'use strict';
var items=document.querySelectorAll('.mn-link-item[data-mega]'),ct=null;
items.forEach(function(i){
i.addEventListener('mouseenter',function(){clearTimeout(ct);items.forEach(function(x){x.classList.remove('mn-open')});i.classList.add('mn-open')});
i.addEventListener('mouseleave',function(){ct=setTimeout(function(){i.classList.remove('mn-open')},200)});
var m=i.querySelector('.mn-mega');
if(m){m.addEventListener('mouseenter',function(){clearTimeout(ct)});m.addEventListener('mouseleave',function(){ct=setTimeout(function(){i.classList.remove('mn-open')},200)})}
});
document.addEventListener('click',function(e){if(!e.target.closest('.mn-link-item[data-mega]'))items.forEach(function(i){i.classList.remove('mn-open')})});
document.addEventListener('keydown',function(e){if(e.key==='Escape'){items.forEach(function(i){i.classList.remove('mn-open')});var mb=document.getElementById('mnMobile'),hb=document.querySelector('.mn-hamburger');if(mb&&mb.classList.contains('mn-active')){mb.classList.remove('mn-active');hb.classList.remove('mn-active');document.body.style.overflow='';mnmShowStep('mnmHome')}}});
var hb=document.querySelector('.mn-hamburger'),md=document.getElementById('mnMobile');
if(hb&&md){hb.addEventListener('click',function(){hb.classList.toggle('mn-active');md.classList.toggle('mn-active');document.body.style.overflow=md.classList.contains('mn-active')?'hidden':'';if(!md.classList.contains('mn-active'))mnmShowStep('mnmHome')})}
})();

function mnmShowStep(id){
document.querySelectorAll('.mnm-step').forEach(function(s){s.classList.remove('mnm-active')});
var el=document.getElementById(id);if(el){el.classList.add('mnm-active');el.scrollTop=0}
var mob=document.getElementById('mnMobile');if(mob)mob.scrollTop=0;
}

var SVC={
cameras:{label:'\u{1F4F9} Security Cameras',nyc:'/security-camera-installation-nyc',brooklyn:'/security-camera-installation-brooklyn-ny',manhattan:'/security-camera-installation-manhattan-ny',queens:'/security-camera-installation-queens-ny',bronx:'/security-camera-installation-bronx-ny',statenisland:'/security-camera-installation-staten-island-ny',longisland:'/security-camera-installation-long-island-ny',nassau:'/security-camera-installation-nassau-county-ny',suffolk:'/security-camera-installation-suffolk-county-ny',hudsonvalley:'/security-camera-installation-hudson-valley-ny',westchester:'/security-camera-installation-westchester-county-ny',rockland:'/security-camera-installation-rockland-county-ny',orange:'/security-camera-installation-orange-county-ny',putnam:'/security-camera-installation-putnam-county-ny',dutchess:'/security-camera-installation-dutchess-county-ny',ulster:'/security-camera-installation-ulster-county-ny'},
wirelesscameras:{label:'\u{1F4F6} Wireless Cameras',nyc:'/wireless-camera-installation-nyc',manhattan:'/wireless-camera-installation-manhattan',hudsonvalley:'/wireless-camera-installation-hudson-valley'},
intercoms:{label:'\u{1F6AA} Intercoms',nyc:'/intercom-installation-nyc',brooklyn:'/intercom-installation-brooklyn-ny',manhattan:'/intercom-installation-manhattan-ny',queens:'/intercom-installation-queens-ny',bronx:'/intercom-installation-bronx-ny',statenisland:'/intercom-installation-staten-island-ny',longisland:'/intercom-installation-long-island-ny',nassau:'/intercom-installation-nassau-county-new-york',suffolk:'/intercom-installation-suffolk-county-new-york',hudsonvalley:'/intercom-installation-hudson-valley-ny',westchester:'/intercom-installation-westchester-new-york',rockland:'/intercom-installation-rockland-county-ny',orange:'/intercom-installation-orange-county-ny',putnam:'/intercom-installation-putnam-county-ny',dutchess:'/intercom-installation-dutchess-county-ny',ulster:'/intercom-installation-ulster-county-ny'},
buzzers:{label:'\u{1F514} Door Buzzer Repair',nyc:'/door-buzzer-repair-nyc',brooklyn:'/door-buzzer-repair-brooklyn-new-york',manhattan:'/door-buzzer-repair-manhattan-new-york',queens:'/door-buzzer-repair-queens-new-york',bronx:'/door-buzzer-repair-bronx-new-york',statenisland:'/door-buzzer-repair-staten-island-new-york',longisland:'/door-buzzer-repair-long-island-ny',nassau:'/door-buzzer-repair-nassau-county-new-york',suffolk:'/door-buzzer-repair-suffolk-county-new-york',hudsonvalley:'/door-buzzer-repair-hudson-valley-ny',westchester:'/door-buzzer-repair-westchester-county',rockland:'/door-buzzer-repair-rockland-county',orange:'/door-buzzer-repair-orange-county-new-york',putnam:'/door-buzzer-repair-putnam-county-new-york',dutchess:'/door-buzzer-repair-dutchess-county-new-york',ulster:'/door-buzzer-repair-ulster-county-new-york'},
alarms:{label:'\u{1F6A8} Alarm Installation',nyc:'/alarm-installation-nyc',brooklyn:'/alarm-installation-brooklyn',manhattan:'/alarm-installation-manhattan',queens:'/alarm-installation-queens',bronx:'/alarm-installation-bronx',statenisland:'/alarm-installation-staten-island',longisland:'/alarm-installation-long-island',nassau:'/alarm-installation-nassau-county',suffolk:'/alarm-installation-suffolk-county',hudsonvalley:'/alarm-installation-hudson-valley',westchester:'/alarm-installation-westchester-county',rockland:'/alarm-installation-rockland-county',orange:'/alarm-installation-orange-county',putnam:'/alarm-installation-putnam-county',dutchess:'/alarm-installation-dutchess-county',ulster:'/alarm-installation-ulster-county'},
firealarms:{label:'\u{1F525} Fire Alarms',nyc:'/fire-alarm-installation-nyc',brooklyn:'/fire-alarm-installation-brooklyn-ny',manhattan:'/fire-alarm-installation-manhattan-ny',queens:'/fire-alarm-installation-queens-new-york',bronx:'/fire-alarm-installation-bronx-ny',statenisland:'/fire-alarm-installation-staten-island-ny',longisland:'/fire-alarm-installation-long-island-ny',nassau:'/fire-alarm-installation-nassau-county-ny',suffolk:'/fire-alarm-installation-suffolk-county-ny',hudsonvalley:'/fire-alarm-installation-hudson-valley-ny',westchester:'/fire-alarm-installation-westchester-county-new-york',rockland:'/fire-alarm-installation-rockland-county-ny',orange:'/fire-alarm-installation-orange-county-ny',putnam:'/fire-alarm-installation-putnam-county-ny',dutchess:'/fire-alarm-installation-dutchess-county-ny',ulster:'/fire-alarm-installation-ulster-county-ny'},
cabling:{label:'\u26A1 Structured Cabling',nyc:'/structured-cabling-installation-nyc',brooklyn:'/structured-cabling-installation-brooklyn',manhattan:'/structured-cabling-installation-manhattan',queens:'/structured-cabling-installation-queens',bronx:'/structured-cabling-installation-bronx',statenisland:'/structured-cabling-installation-staten-island',longisland:'/structured-cabling-installation-long-island',nassau:'/structured-cabling-installation-nassau-county',suffolk:'/structured-cabling-installation-suffolk-county',hudsonvalley:'/structured-cabling-installation-hudson-valley',westchester:'/structured-cabling-installation-westchester-county',rockland:'/structured-cabling-installation-rockland-county',orange:'/structured-cabling-installation-orange-county',putnam:'/structured-cabling-installation-putnam-county',dutchess:'/structured-cabling-installation-dutchess-county',ulster:'/structured-cabling-installation-ulster-county'},
tv:{label:'\u{1F4FA} TV Installation',nyc:'/tv-installation-nyc',brooklyn:'/tv-installation-brooklyn',manhattan:'/tv-installation-manhattan',queens:'/tv-installation-queens',bronx:'/tv-installation-bronx',statenisland:'/tv-installation-staten-island',longisland:'/tv-installation-long-island',nassau:'/tv-installation-nassau-county',suffolk:'/tv-installation-suffolk-county',hudsonvalley:'/tv-installation-hudson-valley',westchester:'/tv-installation-westchester-county',rockland:'/tv-installation-rockland-county',orange:'/tv-installation-orange-county',putnam:'/tv-installation-putnam-county',dutchess:'/tv-installation-dutchess-county',ulster:'/tv-installation-ulster-county'},
accesscontrol:{label:'\u{1F511} Access Control',nyc:'/access-control-installation-nyc',brooklyn:'/access-control-installation-brooklyn',manhattan:'/access-control-installation-manhattan',queens:'/access-control-installation-queens',bronx:'/access-control-installation-bronx',statenisland:'/access-control-installation-staten-island',longisland:'/access-control-installation-long-island',nassau:'/access-control-installation-nassau-county',suffolk:'/access-control-installation-suffolk-county',hudsonvalley:'/access-control-installation-hudson-valley',westchester:'/access-control-installation-westchester-county',rockland:'/access-control-installation-rockland-county',orange:'/access-control-installation-orange-county',putnam:'/access-control-installation-putnam-county',dutchess:'/access-control-installation-dutchess-county',ulster:'/access-control-installation-ulster-county'},
homeautomation:{label:'\u{1F3E0} Home Automation',nyc:'/home-automation-installation-nyc',brooklyn:'/home-automation-installation-brooklyn',manhattan:'/home-automation-installation-manhattan',queens:'/home-automation-installation-queens',bronx:'/home-automation-installation-bronx',statenisland:'/home-automation-installation-staten-island',longisland:'/home-automation-installation-long-island',nassau:'/home-automation-installation-nassau-county',suffolk:'/home-automation-suffolk-county',hudsonvalley:'/home-automation-installation-hudson-valley',westchester:'/home-automation-installation-westchester-county',rockland:'/home-automation-installation-rockland-county',orange:'/home-automation-installation-orange-county',putnam:'/home-automation-putnam-county',dutchess:'/home-automation-dutchess-county',ulster:'/home-automation-ulster-county'},
hometheater:{label:'\u{1F3AC} Home Theater',nyc:'/free-quote?service=home-theater&area=nyc'},
avsound:{label:'\u{1F50A} AV Sound Installation',nyc:'/av-sound-installation-nyc',hudsonvalley:'/av-sound-installation-hudson-valley',longisland:'/av-sound-installation-long-island',manhattan:'/av-sound-installation-manhattan',brooklyn:'/av-sound-installation-brooklyn',queens:'/av-sound-installation-queens',bronx:'/av-sound-installation-bronx',statenisland:'/av-sound-installation-staten-island',nassau:'/av-sound-installation-nassau-county',suffolk:'/av-sound-installation-suffolk-county',westchester:'/av-sound-installation-westchester-county',rockland:'/av-sound-installation-rockland-county',orange:'/av-sound-installation-orange-county',putnam:'/av-sound-installation-putnam-county',dutchess:'/av-sound-installation-dutchess-county',ulster:'/av-sound-installation-ulster-county'},
videowall:{label:'\u{1F4FA} Video Wall Installation',nyc:'/video-wall-installation-nyc',hudsonvalley:'/video-wall-installation-hudson-valley',longisland:'/video-wall-installation-long-island',manhattan:'/video-wall-installation-manhattan',brooklyn:'/video-wall-installation-brooklyn',queens:'/video-wall-installation-queens',bronx:'/video-wall-installation-bronx',statenisland:'/video-wall-installation-staten-island',nassau:'/video-wall-installation-nassau-county',suffolk:'/video-wall-installation-suffolk-county',westchester:'/video-wall-installation-westchester-county',rockland:'/video-wall-installation-rockland-county',orange:'/video-wall-installation-orange-county',putnam:'/video-wall-installation-putnam-county',dutchess:'/video-wall-installation-dutchess-county',ulster:'/video-wall-installation-ulster-county'},
solartrailer:{label:'\u{2600}\uFE0F Solar Surveillance Trailer',nyc:'/solar-surveillance-trailer-nyc',brooklyn:'/solar-surveillance-trailer-brooklyn',manhattan:'/solar-surveillance-trailer-manhattan',queens:'/solar-surveillance-trailer-queens',bronx:'/solar-surveillance-trailer-bronx',statenisland:'/solar-surveillance-trailer-staten-island',longisland:'/solar-surveillance-trailer-long-island',nassau:'/solar-surveillance-trailer-nassau-county',suffolk:'/solar-surveillance-trailer-suffolk-county',hudsonvalley:'/solar-surveillance-trailer-hudson-valley',westchester:'/solar-surveillance-trailer-westchester-county',rockland:'/solar-surveillance-trailer-rockland-county',orange:'/solar-surveillance-trailer-orange-county',putnam:'/solar-surveillance-trailer-putnam-county',dutchess:'/solar-surveillance-trailer-dutchess-county',ulster:'/solar-surveillance-trailer-ulster-county'}
};

var AN={nyc:'NYC (All Boroughs)',brooklyn:'Brooklyn',manhattan:'Manhattan',queens:'Queens',bronx:'Bronx',statenisland:'Staten Island',longisland:'Long Island',nassau:'Nassau County',suffolk:'Suffolk County',hudsonvalley:'Hudson Valley',westchester:'Westchester',rockland:'Rockland',orange:'Orange',putnam:'Putnam',dutchess:'Dutchess',ulster:'Ulster'};

var AG=[
{head:'NYC Boroughs',keys:['nyc','brooklyn','manhattan','queens','bronx','statenisland']},
{head:'Long Island',keys:['longisland','nassau','suffolk']},
{head:'Hudson Valley',keys:['hudsonvalley','westchester','rockland','orange','putnam','dutchess','ulster']}
];

function mnmPickService(sk){
var s=SVC[sk];if(!s)return;
document.getElementById('mnmPickedSvc').textContent=s.label;
var l=document.getElementById('mnmSvcAreaList');l.innerHTML='';
AG.forEach(function(g){
var h=document.createElement('div');h.className='mnm-col-head';h.textContent=g.head;l.appendChild(h);
g.keys.forEach(function(k){if(s[k]){var a=document.createElement('a');a.href=s[k];a.className='mnm-area-link';a.textContent=AN[k];l.appendChild(a)}});
});
mnmShowStep('mnmServiceAreas');
}

function mnmPickArea(ak){
document.getElementById('mnmPickedArea').textContent='\u{1F4CD} '+AN[ak];
var l=document.getElementById('mnmAreaSvcList');l.innerHTML='';
['cameras','wirelesscameras','intercoms','buzzers','alarms','firealarms','cabling','tv','accesscontrol','homeautomation','hometheater','avsound','videowall','solartrailer'].forEach(function(sk){
var s=SVC[sk];if(s[ak]){var a=document.createElement('a');a.href=s[ak];a.className='mnm-area-link';a.textContent=s.label;l.appendChild(a)}
});
mnmShowStep('mnmAreaServices');
}

// ── Desktop: hover service → show areas ──
function mnDeskSvc(el){
document.querySelectorAll('.mn-svc-trigger').forEach(function(t){t.classList.remove('mn-svc-active')});
el.classList.add('mn-svc-active');
var sk=el.getAttribute('data-svc'),s=SVC[sk];if(!s)return;
var r=document.getElementById('mnDeskSvcAreas');if(!r)return;
var h='<div class="mn-mega-col-head">Choose your area</div>';
AG.forEach(function(g){
h+='<div class="mn-area-block">';
h+='<div class="mn-mega-col-head mn-area-group">'+g.head+'</div>';
g.keys.forEach(function(k){if(s[k])h+='<a href="'+s[k]+'">'+AN[k]+'</a>'});
h+='</div>';
});
r.innerHTML=h;
}

// ── Desktop: hover area → show services ──

var RPR={
camerarepair:{label:'\ud83d\udcf9 Security Camera Repair',nyc:'/security-camera-repair-nyc',brooklyn:'/security-camera-repair-brooklyn',manhattan:'/security-camera-repair-manhattan',queens:'/security-camera-repair-queens',bronx:'/security-camera-repair-bronx',statenisland:'/security-camera-repair-staten-island',longisland:'/security-camera-repair-long-island',nassau:'/security-camera-repair-nassau-county',suffolk:'/security-camera-repair-suffolk-county',hudsonvalley:'/security-camera-repair-hudson-valley',westchester:'/security-camera-repair-westchester-county',rockland:'/security-camera-repair-rockland-county',orange:'/security-camera-repair-orange-county',putnam:'/security-camera-repair-putnam-county',dutchess:'/security-camera-repair-dutchess-county',ulster:'/security-camera-repair-ulster-county'},
buzzerrepair:{label:'\ud83d\udd14 Door Buzzer Repair',nyc:'/door-buzzer-repair-nyc',brooklyn:'/door-buzzer-repair-brooklyn-new-york',manhattan:'/door-buzzer-repair-manhattan-new-york',queens:'/door-buzzer-repair-queens-new-york',bronx:'/door-buzzer-repair-bronx-new-york',statenisland:'/door-buzzer-repair-staten-island-new-york',longisland:'/door-buzzer-repair-long-island-ny',nassau:'/door-buzzer-repair-nassau-county-new-york',suffolk:'/door-buzzer-repair-suffolk-county-new-york',hudsonvalley:'/door-buzzer-repair-hudson-valley-ny',westchester:'/door-buzzer-repair-westchester-county',rockland:'/door-buzzer-repair-rockland-county',orange:'/door-buzzer-repair-orange-county-new-york',putnam:'/door-buzzer-repair-putnam-county-new-york',dutchess:'/door-buzzer-repair-dutchess-county-new-york',ulster:'/door-buzzer-repair-ulster-county-new-york'},
intercomrepair:{label:'\ud83d\udeaa Intercom Repair',nyc:'/free-quote?service=intercom-repair&area=nyc',brooklyn:'/free-quote?service=intercom-repair&area=brooklyn',manhattan:'/free-quote?service=intercom-repair&area=manhattan',queens:'/free-quote?service=intercom-repair&area=queens',bronx:'/free-quote?service=intercom-repair&area=bronx',statenisland:'/free-quote?service=intercom-repair&area=staten-island',longisland:'/free-quote?service=intercom-repair&area=long-island',nassau:'/free-quote?service=intercom-repair&area=nassau',suffolk:'/free-quote?service=intercom-repair&area=suffolk',hudsonvalley:'/free-quote?service=intercom-repair&area=hudson-valley',westchester:'/free-quote?service=intercom-repair&area=westchester',rockland:'/free-quote?service=intercom-repair&area=rockland',orange:'/free-quote?service=intercom-repair&area=orange',putnam:'/free-quote?service=intercom-repair&area=putnam',dutchess:'/free-quote?service=intercom-repair&area=dutchess',ulster:'/free-quote?service=intercom-repair&area=ulster'},
alarmrepair:{label:'\ud83d\udea8 Alarm Repair',nyc:'/free-quote?service=alarm-repair&area=nyc',brooklyn:'/free-quote?service=alarm-repair&area=brooklyn',manhattan:'/free-quote?service=alarm-repair&area=manhattan',queens:'/free-quote?service=alarm-repair&area=queens',bronx:'/free-quote?service=alarm-repair&area=bronx',statenisland:'/free-quote?service=alarm-repair&area=staten-island',longisland:'/free-quote?service=alarm-repair&area=long-island',nassau:'/free-quote?service=alarm-repair&area=nassau',suffolk:'/free-quote?service=alarm-repair&area=suffolk',hudsonvalley:'/free-quote?service=alarm-repair&area=hudson-valley',westchester:'/free-quote?service=alarm-repair&area=westchester',rockland:'/free-quote?service=alarm-repair&area=rockland',orange:'/free-quote?service=alarm-repair&area=orange',putnam:'/free-quote?service=alarm-repair&area=putnam',dutchess:'/free-quote?service=alarm-repair&area=dutchess',ulster:'/free-quote?service=alarm-repair&area=ulster'},
firealarmrepair:{label:'\ud83d\udd25 Fire Alarm Repair',nyc:'/free-quote?service=fire-alarm-repair&area=nyc',brooklyn:'/free-quote?service=fire-alarm-repair&area=brooklyn',manhattan:'/free-quote?service=fire-alarm-repair&area=manhattan',queens:'/free-quote?service=fire-alarm-repair&area=queens',bronx:'/free-quote?service=fire-alarm-repair&area=bronx',statenisland:'/free-quote?service=fire-alarm-repair&area=staten-island',longisland:'/free-quote?service=fire-alarm-repair&area=long-island',nassau:'/free-quote?service=fire-alarm-repair&area=nassau',suffolk:'/free-quote?service=fire-alarm-repair&area=suffolk',hudsonvalley:'/free-quote?service=fire-alarm-repair&area=hudson-valley',westchester:'/free-quote?service=fire-alarm-repair&area=westchester',rockland:'/free-quote?service=fire-alarm-repair&area=rockland',orange:'/free-quote?service=fire-alarm-repair&area=orange',putnam:'/free-quote?service=fire-alarm-repair&area=putnam',dutchess:'/free-quote?service=fire-alarm-repair&area=dutchess',ulster:'/free-quote?service=fire-alarm-repair&area=ulster'}
};

function mnDeskRepair(el){
document.querySelectorAll('.mn-rpr-trigger').forEach(function(t){t.classList.remove('mn-svc-active')});
el.classList.add('mn-svc-active');
var rk=el.getAttribute('data-rpr'),s=RPR[rk];if(!s)return;
var r=document.getElementById('mnDeskRepairAreas');if(!r)return;
var h='<div class="mn-mega-col-head">Choose your area</div>';
AG.forEach(function(g){
h+='<div class="mn-area-block">';
h+='<div class="mn-mega-col-head mn-area-group">'+g.head+'</div>';
g.keys.forEach(function(k){if(s[k])h+='<a href="'+s[k]+'">'+AN[k]+'</a>'});
h+='</div>';
});
r.innerHTML=h;
}

function mnmPickRepair(rk){
var s=RPR[rk];if(!s)return;
document.getElementById('mnmPickedSvc').textContent=s.label;
var l=document.getElementById('mnmSvcAreaList');l.innerHTML='';
AG.forEach(function(g){
var h=document.createElement('div');h.className='mnm-col-head';h.textContent=g.head;l.appendChild(h);
g.keys.forEach(function(k){if(s[k]){var a=document.createElement('a');a.href=s[k];a.className='mnm-area-link';a.textContent=AN[k];l.appendChild(a)}});
});
mnmShowStep('mnmServiceAreas');
}

function mnDeskArea(el){
document.querySelectorAll('.mn-area-trigger').forEach(function(t){t.classList.remove('mn-svc-active')});
el.classList.add('mn-svc-active');
var ak=el.getAttribute('data-area');
var r=document.getElementById('mnDeskAreaSvcs');if(!r)return;
var h='<div class="mn-mega-col-head">Services in '+AN[ak]+'</div>';
['cameras','wirelesscameras','intercoms','buzzers','alarms','firealarms','cabling','tv','accesscontrol','homeautomation','hometheater','avsound','videowall','solartrailer'].forEach(function(sk){
var s=SVC[sk];if(s[ak])h+='<a href="'+s[ak]+'">'+s.label+'</a>';
});
r.innerHTML=h;
}

// ── Pricing URL maps ──
var PRICE={
cam:{label:'📹 Camera Pricing',brooklyn:'/security-camera-pricing-brooklyn',manhattan:'/security-camera-pricing-manhattan',queens:'/security-camera-pricing-queens',bronx:'/security-camera-pricing-bronx',statenisland:'/security-camera-pricing-staten-island',nassau:'/security-camera-pricing-nassau-county',suffolk:'/security-camera-pricing-suffolk-county',westchester:'/security-camera-pricing-westchester-county',rockland:'/security-camera-pricing-rockland-county',orange:'/security-camera-pricing-orange-county',putnam:'/security-camera-pricing-putnam-county',dutchess:'/security-camera-pricing-dutchess-county',ulster:'/security-camera-pricing-ulster-county'},
cable:{label:'⚡ Cabling Pricing',brooklyn:'/structured-cabling-pricing-brooklyn',manhattan:'/structured-cabling-pricing-manhattan',queens:'/structured-cabling-pricing-queens',bronx:'/structured-cabling-pricing-bronx',statenisland:'/structured-cabling-pricing-staten-island',nassau:'/structured-cabling-pricing-nassau-county',suffolk:'/structured-cabling-pricing-suffolk-county',westchester:'/structured-cabling-pricing-westchester-county',rockland:'/structured-cabling-pricing-rockland-county',orange:'/structured-cabling-pricing-orange-county',putnam:'/structured-cabling-pricing-putnam-county',dutchess:'/structured-cabling-pricing-dutchess-county',ulster:'/structured-cabling-pricing-ulster-county'},
intercom:{label:'🚪 Intercom Pricing',_single:'/intercom-pricing'},
buzzer:{label:'🔔 Buzzer Repair Pricing',_single:'/door-buzzer-repair-pricing'},
tvprice:{label:'📺 TV Mounting Pricing',nyc:'/tv-mounting-prices-nyc',brooklyn:'/tv-mounting-prices-brooklyn',manhattan:'/tv-mounting-prices-manhattan',queens:'/tv-mounting-prices-queens',bronx:'/tv-mounting-prices-bronx',statenisland:'/tv-mounting-prices-staten-island',longisland:'/tv-mounting-prices-long-island',nassau:'/tv-mounting-prices-nassau-county',suffolk:'/tv-mounting-prices-suffolk-county',hudsonvalley:'/tv-mounting-prices-hudson-valley',westchester:'/tv-mounting-prices-westchester-county',rockland:'/tv-mounting-prices-rockland-county',orange:'/tv-mounting-prices-orange-county',putnam:'/tv-mounting-prices-putnam-county',dutchess:'/tv-mounting-prices-dutchess-county',ulster:'/tv-mounting-prices-ulster-county'}
};

var PRICE_AG=[
{head:'NYC Boroughs',keys:['nyc','brooklyn','manhattan','queens','bronx','statenisland']},
{head:'Long Island',keys:['longisland','nassau','suffolk']},
{head:'Hudson Valley',keys:['hudsonvalley','westchester','rockland','orange','putnam','dutchess','ulster']}
];

// Desktop: hover pricing service → show area pages
function mnDeskPrice(el){
document.querySelectorAll('.mn-price-trigger').forEach(function(t){t.classList.remove('mn-svc-active')});
el.classList.add('mn-svc-active');
var pk=el.getAttribute('data-price');if(!pk)return;
var p=PRICE[pk];if(!p)return;
var r=document.getElementById('mnDeskPriceAreas');if(!r)return;
// Single-page pricing (intercom, buzzer) — just redirect
if(p._single){window.location.href=p._single;return}
var h='<div class="mn-mega-col-head">Select your area</div>';
PRICE_AG.forEach(function(g){
h+='<div class="mn-mega-col-head mn-area-group">'+g.head+'</div>';
g.keys.forEach(function(k){if(p[k])h+='<a href="'+p[k]+'">'+AN[k]+'</a>'});
});
r.innerHTML=h;
}

// Mobile: pick pricing service → show area step
function mnmPickPricing(pk){
var p=PRICE[pk];if(!p)return;
if(p._single){window.location.href=p._single;return}
document.getElementById('mnmPickedPrice').textContent=p.label;
var l=document.getElementById('mnmPriceAreaList');l.innerHTML='';
PRICE_AG.forEach(function(g){
var h=document.createElement('div');h.className='mnm-col-head';h.textContent=g.head;l.appendChild(h);
g.keys.forEach(function(k){if(p[k]){var a=document.createElement('a');a.href=p[k];a.className='mnm-area-link';a.textContent=AN[k];l.appendChild(a)}});
});
mnmShowStep('mnmPricingAreas');
}

/* Google Preferred Source button (Oct 13 2026) - one band above the footer on every page */
(function(){
function add(){
if(document.getElementById('aessPrefSrc'))return;
var b=document.createElement('div');b.id='aessPrefSrc';
b.style.cssText='background:#f8fafc;border-top:1px solid #e5e7eb;padding:22px 16px;text-align:center;font-family:inherit';
b.innerHTML='<div style="font-weight:700;font-size:1rem;color:#111827;margin-bottom:4px">See us first on Google</div>'+
'<div style="font-size:.88rem;color:#4b5563;margin:0 auto 12px;max-width:560px">Add Abstract Enterprises as a preferred source and Google shows our tips and updates to you first in Top Stories and AI answers.</div>'+
'<div style="display:flex;justify-content:center"><div google-add-preferred-source-btn data-lang="en"></div></div>'+
'<noscript><a href="https://www.google.com/preferences/source?q=abstractenterprisessecuritysystems.com">Add as a preferred source on Google</a></noscript>';
var f=document.querySelector('footer');
if(f&&f.parentNode)f.parentNode.insertBefore(b,f);else document.body.appendChild(b);
var s=document.createElement('script');s.async=true;s.src='https://news.google.com/swg/js/v1/publisher.js';
s.onerror=function(){var d=b.querySelector('[google-add-preferred-source-btn]');if(d)d.outerHTML='<a href="https://www.google.com/preferences/source?q=abstractenterprisessecuritysystems.com" target="_blank" rel="noopener" style="display:inline-block;padding:10px 18px;border:1px solid #d1d5db;border-radius:999px;background:#fff;color:#1f2937;font-weight:600;text-decoration:none">Add as a preferred source on Google</a>'};
document.head.appendChild(s);
}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',add);else add();
})();

/* TV Mounting Pricing menu entry (added at runtime so page HTML stays untouched) */
(function(){function add(){
var b=document.querySelector('.mn-price-trigger[data-price="buzzer"]');
if(b&&!document.querySelector('.mn-price-trigger[data-price="tvprice"]')){var a=document.createElement('a');a.className='mn-price-trigger';a.setAttribute('data-price','tvprice');a.setAttribute('onclick','mnDeskPrice(this)');a.textContent='\uD83D\uDCFA TV Mounting Pricing';b.parentNode.insertBefore(a,b.nextSibling);}
var m=document.querySelector('button[onclick="mnmPickPricing(\'cam\')"]');
if(m&&!document.querySelector('button[onclick="mnmPickPricing(\'tvprice\')"]')){var c=m.cloneNode(true);c.setAttribute('onclick',"mnmPickPricing('tvprice')");c.innerHTML='\uD83D\uDCFA TV Mounting Pricing<span class="mnm-path-arrow">&rsaquo;</span>';m.parentNode.insertBefore(c,m.nextSibling);}
}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',add);else add();})();

/* TV pages: sticky bar was falling back to the homepage set (Build Your System -> /alarm-calculator). Swap in TV content. */
(function(){function fix(){
var p=location.pathname.toLowerCase();if(!/\/tv-(installation|mounting)/.test(p)||p.indexOf('policies')>-1)return;
var tr=document.getElementById('spbTrack'),ct=document.getElementById('spbCta'),lb=document.getElementById('spbLabelText');if(!tr||!ct)return;
var Z=[['brooklyn',179.99,'brooklyn'],['bronx',209.99,'bronx'],['queens',179.99,'queens'],['staten-island',209.99,'staten-island'],['manhattan',244.99,'manhattan'],
['nassau',209.99,'nassau-county'],['long-island',209.99,'long-island'],['suffolk',229.99,'suffolk-county'],['westchester',219.99,'westchester-county'],['rockland',219.99,'rockland-county'],
['orange',229.99,'orange-county'],['putnam',229.99,'putnam-county'],['dutchess',254.99,'dutchess-county'],['ulster',254.99,'ulster-county'],['hudson-valley',219.99,'hudson-valley']];
var b=179.99,pg='nyc';for(var i=0;i<Z.length;i++){if(p.indexOf(Z[i][0])>-1){b=Z[i][1];pg=Z[i][2];break;}}
function f(x){return '$'+x.toFixed(2)}
var priceUrl='/tv-mounting-prices-'+pg,calc=document.getElementById('aessTvCalc');
var chips=[['📺 32″–55″','Flat or tilt, drywall','from '+f(b),'spb-chip--gold'],['56″–65″ TV','Flat or tilt mount',f(b+30),''],['66″–75″ TV','Flat or tilt mount',f(b+60),''],
['76″–85″ TV','Flat or tilt mount',f(b+100),''],['86″–97″ TV','Two technicians',f(b+175),''],['98″+ TV','Two technicians',f(b+220),''],
['🧱 Metal Studs','Drywall wall','+$30',''],['🧱 Plaster','Prewar walls','+$45',''],['🧱 Brick / Stone','Masonry anchors','+$65',''],['🧱 Concrete / Block','Hammer drill','+$75',''],['🧱 Tile / Marble','Diamond bits','+$95',''],
['↔️ Full-Motion','Articulating mount','+$40',''],['📐 Corner Mount','Corner install','+$40',''],['🖼 Frame / Art TV','Flush gallery look','+$70',''],['⬆️ Ceiling Mount','Bedrooms, bars','+$85',''],['☀️ Outdoor TV','Patio / deck','+$90',''],
['🔥 Over Fireplace','Fixed or tilt','+$130',''],['🔥 Pull-Down Fireplace','Brings it to eye level','+$160',''],
['🔌 Hidden Wires','In-wall power & cable kit','$169','spb-chip--green'],['🔌 Cord Cover','Paintable, on the wall','$59',''],['🔗 Cable Run','HDMI / Ethernet, 25 ft','$99',''],
['🔊 Soundbar','Placed / wall-mounted','$79 / $129',''],['📡 Streaming / Console','Setup, each','$49',''],['🎛 A/V Receiver','Receiver & speakers','$129',''],['🔈 Sonos','Wireless surround','$125',''],
['🎮 Universal Remote','Programming','$99',''],['🎬 Home Theater','Full setup','$350',''],['⬇️ Take Down Old TV','Old bracket removal $45','$85',''],['🪵 Backer Board','Big TVs, weak walls','$85',''],
['🪜 High Mount','Above ~8 ft','$75',''],['🪜 Walk-Up','3rd floor+, no elevator','$40',''],['♻️ Haul Away','Old TV recycled','$79',''],['📦 Box Removal','Take the packaging','$25',''],
['📄 COI','For your building','Free','spb-chip--green'],['📋 Licensed','NYS Lic. #12000287431','Insured','']];
if(p.indexOf('manhattan')>-1&&p.indexOf('manhattan-beach')<0)chips.splice(1,0,['🚗 Manhattan Parking','Flat, every job','$150','']);
var h='';for(var r=0;r<2;r++)for(var j=0;j<chips.length;j++){var c=chips[j];h+='<a href="'+(calc?'#aessTvCalc':priceUrl)+'" class="spb-chip '+c[3]+'"><span class="spb-chip-tag">'+c[0]+'</span><span class="spb-chip-mid">'+c[1]+'</span><span class="spb-chip-val">'+c[2]+'</span></a><span class="spb-chip-div"></span>';}
tr.style.animationDuration=(chips.length*4.5)+'s';
tr.innerHTML=h;if(lb)lb.textContent='TV Mounting';
var a=ct.querySelector('.spb-btn-primary');if(a){a.setAttribute('href',calc?'#aessTvCalc':priceUrl);a.innerHTML=a.innerHTML.replace(/Build Your System|Get Free Quote|Free Quote/,'See My TV Price');if(a.textContent.indexOf('See My TV Price')<0)a.textContent='See My TV Price';}
}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',fix);else fix();})();
