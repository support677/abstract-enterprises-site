function main(){
var LIST='AESS Auto - camera shoppers + brands';
var BRANDS=['ring camera','ring cameras','ring doorbell','ring alarm','ring app','arlo','blink camera','blink cameras','blink app','wyze','eufy','eufycam','nest camera','nest cam','nest doorbell','google nest','tapo','tp link','tp-link','kasa','reolink','lorex','swann','zosi','night owl','annke','amcrest','hikvision','hik vision','dahua','uniview','unv','axis camera','hanwha','wisenet','ubiquiti','unifi','verkada','avigilon','imou','ezviz','simplisafe','simpli safe','adt','vivint','defender camera','funlux','sv3c','botslab','alkivision','honest view','watchnet','digital watchdog','flir','foscam','blurams','aosu','toucan camera','canary camera','abode','xiaomi','yi home','vicohome','momentum camera','geeni','merkury','litmor','galayou','kami camera','cove security','frontpoint','brinks','vector security','abstract enterprises'];
var CAM=/\b(camera|cameras|cam|cams|cctv|surveillance|nvr|dvr|webcam|webcams)\b/;
var HIRE=/\b(install|installs|installation|installations|installer|installers|installing|installed|setup|set up|mount|mounting|mounted|technician|technicians|tech|techs|contractor|contractors|company|companies|service|services|repair|repairs|repairing|fix|fixing|wiring|wire|rewire|cabling|maintenance|replace|replacement|upgrade|estimate|quote|hire|professional|pro)\b/;
var lst=AdsApp.negativeKeywordLists().withCondition("shared_set.name = '"+LIST+"'").get();
var list=lst.hasNext()?lst.next():AdsApp.newNegativeKeywordListBuilder().withName(LIST).build().getResult();
var have={};var it=list.negativeKeywords().get();while(it.hasNext()){have[it.next().getText().toLowerCase()]=1;}
var add=[];function want(t){t=t.toLowerCase();if(!have[t]){have[t]=1;add.push(t);}}
BRANDS.forEach(function(b){want('"'+b+'"');});
var rows=AdsApp.search("SELECT search_term_view.search_term,metrics.impressions FROM search_term_view WHERE segments.date DURING LAST_30_DAYS AND metrics.impressions > 0");
var shop=0;while(rows.hasNext()){var term=rows.next().searchTermView.searchTerm.toLowerCase().trim();if(CAM.test(term)&&!HIRE.test(term)&&term.length<80){want('['+term+']');shop++;}}
add.forEach(function(t){list.addNegativeKeyword(t);});
var attached=0,skipped=[];var cs=AdsApp.campaigns().withCondition("campaign.status = ENABLED").withCondition("campaign.advertising_channel_type = SEARCH").get();
while(cs.hasNext()){var c=cs.next();var nm=c.getName().toLowerCase();var b=BRANDS.filter(function(x){return new RegExp('\\b'+x.replace(/[-]/g,'\\-')+'\\b').test(nm);});if(b.length){skipped.push(c.getName());continue;}
var on=false;var li=c.negativeKeywordLists().get();while(li.hasNext()){if(li.next().getName()==LIST){on=true;break;}}if(!on){c.addNegativeKeywordList(list);attached++;}}
Logger.log('added '+add.length+' negatives ('+shop+' shopper terms seen) | newly attached to '+attached+' campaigns | skipped brand-named: '+skipped.join('; '));
Logger.log('ADDED: '+add.join(' , ').slice(0,4000));
}