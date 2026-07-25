/* ============================================================
   ABSTRACT ENTERPRISES — SHARED SCALABLE QUOTE BUILDER
   One module, injected on every camera page that exposes window.__qb.
   Reads the page's own CAMS / mult / areaName / payArea / brand.
   Edit rates HERE once -> updates every page.
   ============================================================ */
(function(){
  // ---- Editable rates (one place, sitewide) ----
  var RATE_CONCEAL = 125;            // per camera, in-wall concealment (NYC brick/plaster)
  var STORAGE = [                    // [label, addCost]
    ["Standard NVR + included drive (~2 weeks)",0],
    ["+ 4TB \u00b7 ~30 days retention (+$350)",350],
    ["+ 8TB \u00b7 ~60 days retention (+$650)",650],
    ["+ 16TB \u00b7 ~90 days retention (+$1,150)",1150],
    ["+ 32TB RAID \u00b7 ~120+ days (+$2,100)",2100]
  ];
  // Warranty scales automatically with the build. Customer never sees a percentage.
  // [label, pct-internal] -> dollar amount is computed live and shown in the dropdown.
  var WARRANTY = [
    ["2-week system warranty (included)",0],
    ["3-Year Extended Coverage",0.06],
    ["5-Year Extended Coverage",0.10]
  ];
  var LONGRUN = [                    // [label, perLongCam]
    ["All runs under 100 ft (standard)",0],
    ["Some runs 100\u2013200 ft (+$75/long camera)",75],
    ["Some runs 200\u2013300 ft + PoE extender/midspan (+$150/long camera)",150]
  ];
  var WEB3KEY = "88890030-1770-483e-a622-0e054d8e14b1";

  function money(n){return '$'+Math.round(n).toLocaleString();}
  function Q(){return window.__qb||{};}                 // page data hook
  function CAMS(){return Q().CAMS||[];}
  function mult(){var m=Q().mult;return (m&&m>0)?m:1.00;}
  function area(){return Q().areaName||'Brooklyn';}
  function payArea(){return Q().payArea||'brooklyn';}
  function brand(){return Q().brand||'Camera';}
  function pageName(){return Q().pageName||document.title;}

  function buildHTML(){
    var c='';
    STORAGE.forEach(function(o,i){c+='<option value="'+o[1]+'">'+o[0]+'</option>';});
    var w='';WARRANTY.forEach(function(o,i){w+='<option value="'+o[1]+'" data-wlabel="'+o[0]+'">'+o[0]+'</option>';});
    var l='';LONGRUN.forEach(function(o,i){l+='<option value="'+o[1]+'">'+o[0]+'</option>';});
    return ''+
'<div id="qb-wrap" style="margin:8px 0 26px;border:2px solid #c0392b;border-radius:16px;padding:20px 22px;background:linear-gradient(180deg,#fff,#fbfcfe)">'+
'<div style="display:flex;align-items:center;gap:8px;margin-bottom:4px"><span style="font-weight:900;color:#c0392b;font-size:1.15rem">Build &amp; Price Your System</span><span id="qb-area-tag" style="background:#c0392b;color:#fff;font-size:.72rem;font-weight:800;padding:3px 9px;border-radius:20px"></span></div>'+
'<p style="margin:0 0 16px;color:#666;font-size:.88rem">Scale to any size &mdash; 4 cameras or 40+. Pricing updates live for your area. Add concealment, storage, warranty and long cable runs, then pay your deposit online.</p>'+
'<div style="display:grid;grid-template-columns:1fr;gap:14px">'+
'<div><label class="qb-lab">1. Camera model</label><select id="qb-model" class="qb-sel"></select></div>'+
'<div><label class="qb-lab">2. Number of cameras</label><div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap">'+
'<button type="button" onclick="QB.step(-1)" class="qb-pm">&minus;</button>'+
'<input id="qb-qty" type="number" min="1" max="200" value="4" inputmode="numeric" style="width:90px;text-align:center;padding:11px;border:1px solid #cfd8e6;border-radius:10px;font-size:1.1rem;font-weight:800;color:#1f2d4d">'+
'<button type="button" onclick="QB.step(1)" class="qb-pm">+</button>'+
'<div style="display:flex;gap:6px;flex-wrap:wrap;margin-left:6px">'+
'<button type="button" onclick="QB.set(8)" class="qb-quick">8</button><button type="button" onclick="QB.set(16)" class="qb-quick">16</button><button type="button" onclick="QB.set(24)" class="qb-quick">24</button><button type="button" onclick="QB.set(40)" class="qb-quick">40</button></div></div></div>'+
'<div><label class="qb-lab">3. Recorder &amp; storage retention</label><select id="qb-storage" class="qb-sel">'+c+'</select></div>'+
'<div><label class="qb-lab">4. Warranty</label><select id="qb-warranty" class="qb-sel">'+w+'</select></div>'+
'<div style="background:#f6f8fb;border-radius:10px;padding:12px 14px"><label style="display:flex;align-items:center;gap:10px;cursor:pointer;font-weight:700;color:#1f2d4d;font-size:.92rem"><input id="qb-conceal" type="checkbox" style="width:20px;height:20px;accent-color:#c0392b">In-wall cable concealment &mdash; no exposed wire, brick/plaster (+$'+RATE_CONCEAL+'/camera)</label></div>'+
'<div><label class="qb-lab">5. Long cable runs (100&ndash;300 ft)</label><select id="qb-longrun" class="qb-sel">'+l+'</select>'+
'<input id="qb-longqty" type="number" min="0" max="200" value="0" placeholder="how many cameras need a long run?" style="width:100%;margin-top:8px;padding:10px;border:1px solid #cfd8e6;border-radius:10px;font-size:.9rem;font-weight:600;color:#1f2d4d">'+
'<p style="margin:5px 0 0;color:#9aa3b2;font-size:.78rem">300 ft is the max PoE run; beyond that we stage a powered extender/midspan, included in the 200&ndash;300 ft tier.</p></div>'+
'</div>'+
'<div style="margin-top:18px;padding-top:16px;border-top:2px dashed #e2e7ef">'+
'<div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:2px"><span style="color:#666;font-size:.9rem">Estimated installed total</span><span id="qb-total" style="font-weight:900;font-size:1.9rem;color:#c0392b">$0</span></div>'+
'<div id="qb-break" style="color:#9aa3b2;font-size:.8rem;line-height:1.7"></div>'+
'<div style="display:flex;justify-content:space-between;margin-top:8px;font-size:.9rem"><span style="color:#1f2d4d;font-weight:800">50% deposit to book</span><span id="qb-dep" style="font-weight:900;color:#1f2d4d">$0</span></div></div>'+
'<div id="qb-lead" style="margin-top:16px;background:#f6f8fb;border-radius:12px;padding:14px 16px">'+
'<div style="font-weight:800;color:#1f2d4d;font-size:.9rem;margin-bottom:8px">Email me this quote &amp; lock the price</div>'+
'<div style="display:grid;grid-template-columns:1fr 1fr;gap:8px">'+
'<input id="qb-name" type="text" placeholder="Name" class="qb-in"><input id="qb-phone" type="tel" placeholder="Phone" class="qb-in">'+
'<input id="qb-email" type="email" placeholder="Email" class="qb-in" style="grid-column:1/3"></div>'+
'<button type="button" onclick="QB.lead()" id="qb-lead-btn" style="width:100%;margin-top:8px;background:#1f2d4d;color:#fff;font-weight:800;padding:12px;border:0;border-radius:8px;cursor:pointer;font-size:.92rem">Send Me This Quote &rarr;</button>'+
'<div id="qb-lead-msg" style="margin-top:8px;font-size:.82rem;color:#16a34a;display:none">Sent &mdash; we&#x2019;ll follow up shortly. You can also pay your deposit below.</div></div>'+
'<div style="display:flex;gap:10px;margin-top:16px;flex-wrap:wrap">'+
'<a id="qb-pay" href="#" style="flex:1;min-width:200px;text-align:center;background:#c0392b;color:#fff;font-weight:900;padding:15px;border-radius:12px;text-decoration:none;font-size:1rem">Pay 50% Deposit &amp; Book &rarr;</a>'+
'<a id="qb-call" href="tel:3479348335" style="flex:1;min-width:160px;text-align:center;background:#1f2d4d;color:#fff;font-weight:800;padding:15px;border-radius:12px;text-decoration:none;font-size:1rem">Call (347) 934-8335</a></div>'+
'<p style="margin:10px 0 0;color:#9aa3b2;font-size:.78rem">Estimate only &mdash; final price confirmed at your free site walkthrough before any work starts. County sales tax added at checkout.</p>'+
'<style>.qb-lab{font-weight:800;color:#1f2d4d;font-size:.92rem;display:block;margin-bottom:6px}.qb-sel{width:100%;padding:11px;border:1px solid #cfd8e6;border-radius:10px;font-size:.95rem;font-weight:600;color:#1f2d4d;background:#fff}.qb-in{padding:10px;border:1px solid #cfd8e6;border-radius:8px;font-size:.88rem}.qb-pm{width:46px;height:46px;border:1px solid #cfd8e6;background:#f6f8fb;border-radius:10px;font-size:1.4rem;font-weight:800;cursor:pointer;color:#1f2d4d}.qb-quick{background:#fff;border:1px solid #cfd8e6;border-radius:8px;padding:8px 11px;font-weight:800;cursor:pointer;color:#1f2d4d;font-size:.85rem}.qb-quick:hover{background:#c0392b;color:#fff;border-color:#c0392b}</style>'+
'</div>';
  }

  function fillModels(){
    var sel=document.getElementById('qb-model');if(!sel)return;
    var cams=CAMS();if(!cams.length)return;
    if(sel.options.length===cams.length){ // just refresh prices/labels
      cams.forEach(function(c,i){sel.options[i].textContent=c[0]+' \u2014 '+money(c[2]*mult())+'/cam installed';});
      return;
    }
    sel.innerHTML='';
    cams.forEach(function(c,i){var o=document.createElement('option');o.value=i;o.textContent=c[0]+' \u2014 '+money(c[2]*mult())+'/cam installed';sel.appendChild(o);});
  }


  function refreshWarranty(subBeforeWarranty){
    var sel=document.getElementById('qb-warranty');if(!sel)return;
    for(var i=0;i<sel.options.length;i++){
      var op=sel.options[i];
      var base=op.getAttribute('data-wlabel')||op.textContent;
      var pct=parseFloat(op.value)||0;
      if(pct>0){
        var amt=Math.round(subBeforeWarranty*pct);
        op.textContent=base+' \u2014 +'+money(amt);
      }else{
        op.textContent=base;
      }
    }
  }

  var QB={
    step:function(d){var q=document.getElementById('qb-qty');q.value=Math.max(1,Math.min(200,(parseInt(q.value)||0)+d));QB.calc();},
    set:function(v){document.getElementById('qb-qty').value=v;QB.calc();},
    calc:function(){
      var cams=CAMS();if(!cams.length)return;
      var cam=cams[parseInt(document.getElementById('qb-model').value)||0]||cams[0];
      var qty=Math.max(1,parseInt(document.getElementById('qb-qty').value)||1);
      var m=mult();
      var base=cam[2]*m*qty;
      var conceal=document.getElementById('qb-conceal').checked?RATE_CONCEAL*qty*m:0;
      var storage=(parseFloat(document.getElementById('qb-storage').value)||0)*m;
      var lr=parseFloat(document.getElementById('qb-longrun').value)||0;
      var lq=Math.min(qty,Math.max(0,parseInt(document.getElementById('qb-longqty').value)||0));
      var longrun=lr*lq*m;
      var sub=base+conceal+storage+longrun;
      refreshWarranty(sub);
      var wr=parseFloat(document.getElementById('qb-warranty').value)||0;
      var warranty=sub*wr;
      var total=sub+warranty;
      document.getElementById('qb-total').textContent=money(total);
      document.getElementById('qb-dep').textContent=money(total*0.5);
      var parts=[qty+'\u00d7 '+cam[0]+' '+money(base)];
      if(conceal)parts.push('concealment '+money(conceal));
      if(storage)parts.push('storage '+money(storage));
      if(longrun)parts.push(lq+' long run '+money(longrun));
      if(warranty)parts.push('warranty '+money(warranty));
      document.getElementById('qb-break').innerHTML=parts.join(' &middot; ');
      document.getElementById('qb-area-tag').textContent=area();
      var desc=qty+'x '+cam[0]+' '+brand()+' install'+(document.getElementById('qb-conceal').checked?' + concealment':'')+(storage?' + storage':'')+(wr?' + ext warranty':'')+' ('+area()+')';
      document.getElementById('qb-pay').href='/pay.html?desc='+encodeURIComponent(desc)+'&amount='+Math.round(total*0.5)+'&area='+encodeURIComponent(payArea());
      // GA4 hook (fires only if gtag present)
      if(typeof gtag==='function'){gtag('event','quote_build',{brand:brand(),area:area(),cameras:qty,value:Math.round(total)});}
    },
    lead:function(){
      var nm=document.getElementById('qb-name').value.trim();
      var ph=document.getElementById('qb-phone').value.trim();
      var em=document.getElementById('qb-email').value.trim();
      if(!nm||(!ph&&!em)){alert('Please add your name and a phone or email.');return;}
      var btn=document.getElementById('qb-lead-btn');btn.textContent='Sending...';btn.disabled=true;
      var cam=CAMS()[parseInt(document.getElementById('qb-model').value)||0];
      var qty=document.getElementById('qb-qty').value;
      var fd=new FormData();
      fd.append('access_key',WEB3KEY);
      fd.append('subject',brand().toUpperCase()+' QUOTE BUILDER LEAD \u2014 '+qty+'x '+cam[0]+' '+document.getElementById('qb-total').textContent+' ('+area()+')');
      fd.append('name',nm);fd.append('phone',ph);fd.append('email',em||'(none)');
      fd.append('Area',area());fd.append('Brand',brand());fd.append('Camera',cam[0]);fd.append('Quantity',qty);
      fd.append('Estimated_Total',document.getElementById('qb-total').textContent);
      fd.append('Deposit',document.getElementById('qb-dep').textContent);
      fd.append('Breakdown',document.getElementById('qb-break').textContent);
      fd.append('Page',pageName());
      fetch('https://api.web3forms.com/submit',{method:'POST',body:fd})
       .then(function(r){return r.json();})
       .then(function(){btn.style.display='none';document.getElementById('qb-lead-msg').style.display='block';if(typeof gtag==='function'){gtag('event','generate_lead',{brand:brand(),area:area()});}})
       .catch(function(){btn.textContent='Send Me This Quote \u2192';btn.disabled=false;alert('Could not send \u2014 please call (347) 934-8335.');});
    }
  };
  window.QB=QB;
  window.qbRefresh=function(){fillModels();QB.calc();};   // call after area change

  function inject(){
    var pkgs=document.getElementById('ubq-pkgs');
    if(!pkgs||document.getElementById('qb-wrap'))return;
    var d=document.createElement('div');d.innerHTML=buildHTML();
    pkgs.parentNode.insertBefore(d.firstChild,pkgs.nextSibling);
    document.addEventListener('change',function(e){if(e.target&&e.target.id&&e.target.id.indexOf('qb-')===0&&e.target.id!=='qb-name'&&e.target.id!=='qb-phone'&&e.target.id!=='qb-email')QB.calc();});
    document.addEventListener('input',function(e){if(e.target&&(e.target.id==='qb-qty'||e.target.id==='qb-longqty'))QB.calc();});
    fillModels();QB.calc();
  }
  if(document.readyState!=='loading')inject();else document.addEventListener('DOMContentLoaded',inject);
})();
