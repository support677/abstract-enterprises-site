function main(){
// Nov 12 2026 rule (Anwar): a brand alone = shopper -> block EXACT. Brand + install/installer/repair = lead -> keep live.
// Only competitor service companies, store names and our own name stay blocked as PHRASE (every search containing them).
var LIST='AESS Auto - camera shoppers + brands';
var ILIST='AESS Neg - intercom/buzzer brands + DIY';
var PHRASE_ALWAYS=['ring alarm','ring app','blink app','simplisafe','simpli safe','adt','vivint','abode','cove security','frontpoint','brinks','vector security','abstract enterprises','best buy'];
var CAM_BRANDS=['ring camera','ring cameras','ring doorbell','arlo','blink camera','blink cameras','wyze','eufy','eufycam','nest camera','nest cam','nest doorbell','google nest','tapo','tp link','tp-link','kasa','reolink','lorex','swann','zosi','night owl','annke','amcrest','hikvision','hik vision','dahua','uniview','unv','axis camera','hanwha','wisenet','ubiquiti','unifi','verkada','avigilon','imou','ezviz','defender camera','funlux','sv3c','botslab','alkivision','honest view','watchnet','digital watchdog','flir','foscam','blurams','aosu','toucan camera','canary camera','xiaomi','yi home','vicohome','momentum camera','geeni','merkury','litmor','galayou','kami camera'];
var ICOM_BRANDS=['akuvox','aiphone','comelit','elvox','siedle','2n','butterflymx','butterfly','lee dan','leedan','dahua','chamberlain','came','abb','fanvil','panasonic','avigilon','tektone','swiftlane','swift lane','smartplus','assaabloy','assa abloy','adams rite','trine','pacific'];
var ICOM_PHRASE_OLD=['akuvox','aiphone','comelit','elvox','siedle','2n intercom','2n indoor','2n ip','butterflymx','butterfly intercom','lee dan','leedan','dahua','chamberlain','came intercom','abb door','fanvil','panasonic','avigilon','tektone','swiftlane','swift lane','smartplus','assaabloy','assa abloy','adams rite','trine','pacific door buzzer'];
var ALLB=PHRASE_ALWAYS.concat(CAM_BRANDS);
var CAM=/\b(camera|cameras|cam|cams|cctv|surveillance|nvr|dvr|webcam|webcams)\b/;
var HIRE=/\b(install|installs|installation|installations|installer|installers|installing|installed|setup|set up|mount|mounting|mounted|technician|technicians|tech|techs|contractor|contractors|company|companies|service|services|repair|repairs|repairing|fix|fixing|wiring|wire|rewire|cabling|maintenance|replace|replacement|upgrade|estimate|quote|hire|professional|pro)\b/;
function getList(n){var l=AdsApp.negativeKeywordLists().withCondition("shared_set.name = '"+n+"'").get();return l.hasNext()?l.next():null;}
function camVariants(b){var v=[b,b+' app'];if(!/(camera|cameras|cam|doorbell)$/.test(b)){v=v.concat([b+' camera',b+' cameras',b+' security camera',b+' security cameras',b+' camera system',b+' doorbell',b+' doorbell camera',b+' nvr',b+' system']);}return v;}
function icomVariants(b){return [b,b+' intercom',b+' intercom system',b+' intercoms',b+' video intercom',b+' doorbell',b+' app',b+' door entry system',b+' access control',b+' indoor monitor',b+' door station'];}
function fixList(list,dropPhrase,keepPhrase,exacts){
  var drop={};dropPhrase.forEach(function(x){drop['"'+x+'"']=1;});
  var have={},removed=[];var it=list.negativeKeywords().get();
  while(it.hasNext()){var k=it.next();var raw=k.getText().toLowerCase().replace(/^["\[]+|["\]]+$/g,'');var mt=String(k.getMatchType()).toUpperCase();var t=mt.indexOf('EXACT')>=0?'['+raw+']':(mt.indexOf('PHRASE')>=0?'"'+raw+'"':raw);if(drop[t]){removed.push(t);k.remove();}else{have[t]=1;}}
  var add=[];function want(t){t=t.toLowerCase();if(!have[t]){have[t]=1;add.push(t);}}
  keepPhrase.forEach(function(b){want('"'+b+'"');});
  exacts.forEach(function(e){want('['+e+']');});
  return {have:have,want:want,add:add,removed:removed};
}
// --- camera list ---
var list=getList(LIST)||AdsApp.newNegativeKeywordListBuilder().withName(LIST).build().getResult();
var ex=[];CAM_BRANDS.forEach(function(b){ex=ex.concat(camVariants(b));});
var C=fixList(list,CAM_BRANDS,PHRASE_ALWAYS,ex);
var rows=AdsApp.search("SELECT search_term_view.search_term,metrics.impressions FROM search_term_view WHERE segments.date DURING LAST_30_DAYS AND metrics.impressions > 0");
var shop=0;while(rows.hasNext()){var term=rows.next().searchTermView.searchTerm.toLowerCase().trim();if(CAM.test(term)&&!HIRE.test(term)&&term.length<80&&term.split(/\s+/).length<=10){C.want('['+term+']');shop++;}}
C.add.forEach(function(t){list.addNegativeKeyword(t);});
// --- intercom/buzzer list ---
var il=getList(ILIST);var I={add:[],removed:[]};
if(il){var iex=[];ICOM_BRANDS.forEach(function(b){iex=iex.concat(icomVariants(b));});I=fixList(il,ICOM_PHRASE_OLD,[],iex);I.add.forEach(function(t){il.addNegativeKeyword(t);});}
// --- attach camera list to enabled search campaigns (skip brand-named) ---
var attached=0,skipped=[];var cs=AdsApp.campaigns().withCondition("campaign.status = ENABLED").withCondition("campaign.advertising_channel_type = SEARCH").get();
while(cs.hasNext()){var c=cs.next();var nm=c.getName().toLowerCase();var b=ALLB.filter(function(x){return new RegExp('\\b'+x.replace(/[-]/g,'\\-')+'\\b').test(nm);});if(b.length){skipped.push(c.getName());continue;}
var on=false;var li=c.negativeKeywordLists().get();while(li.hasNext()){if(li.next().getName()==LIST){on=true;break;}}if(!on){c.addNegativeKeywordList(list);attached++;}}
Logger.log('CAMERA LIST: removed '+C.removed.length+' brand phrase negatives | added '+C.add.length+' ('+shop+' shopper terms seen) | newly attached '+attached+' | skipped brand-named: '+skipped.join('; '));
Logger.log('INTERCOM LIST: removed '+I.removed.length+' brand phrase negatives | added '+I.add.length);
Logger.log('REMOVED: '+C.removed.concat(I.removed).join(' , '));
Logger.log('ADDED: '+C.add.concat(I.add).join(' , ').slice(0,4000));
}
