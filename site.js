// Hevify Labs — shared site behavior (cursor, reveal-on-scroll, page transitions, nav shadow)
(function(){
  var reduceMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Page-load fade-in
  document.documentElement.classList.add('hv-pt-ready');

  // Custom cursor (desktop pointer only)
  (function(){
    var dot=document.getElementById('cDot'), ring=document.getElementById('cRing');
    if(!dot || !ring) return;
    if(!matchMedia('(hover:hover) and (pointer:fine)').matches) return;
    var mx=0,my=0,rx=0,ry=0;
    addEventListener('mousemove',function(e){mx=e.clientX;my=e.clientY;dot.style.left=mx+'px';dot.style.top=my+'px'});
    (function loop(){rx+=(mx-rx)*.18;ry+=(my-ry)*.18;ring.style.left=rx+'px';ring.style.top=ry+'px';requestAnimationFrame(loop)})();
    var hot='a,button,.btn,.service-card,.team-card,.insight-card,.step,summary,.pkg,.whycard,[data-hot]';
    document.querySelectorAll(hot).forEach(function(el){
      el.addEventListener('mouseenter',function(){ring.classList.add('hot')});
      el.addEventListener('mouseleave',function(){ring.classList.remove('hot')});
    });
    addEventListener('mousedown',function(){ring.style.opacity=.5});
    addEventListener('mouseup',function(){ring.style.opacity=1});
  })();

  // Scroll reveal
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){
      es.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); } });
    },{threshold:.12});
    document.querySelectorAll('.reveal').forEach(function(el){ io.observe(el); });
  } else {
    document.querySelectorAll('.reveal').forEach(function(el){ el.classList.add('in'); });
  }

  // Nav shadow on scroll
  var nav=document.getElementById('siteNav') || document.querySelector('.navb');
  if(nav){ addEventListener('scroll',function(){ nav.classList.toggle('scrolled',scrollY>10); }); }

  // Count-up stats
  function countUp(el,t,dec){
    var s=null,d=1400;
    function step(n){ if(!s)s=n; var p=Math.min((n-s)/d,1); var v=t*p; el.textContent=dec?v.toFixed(1):Math.floor(v); if(p<1) requestAnimationFrame(step); }
    requestAnimationFrame(step);
  }
  if('IntersectionObserver' in window){
    var co=new IntersectionObserver(function(es){
      es.forEach(function(e){ if(e.isIntersecting){ var el=e.target; countUp(el,parseFloat(el.dataset.count),el.classList.contains('count-decimal')); co.unobserve(el); } });
    },{threshold:.5});
    document.querySelectorAll('.count,.count-decimal').forEach(function(el){ co.observe(el); });
  }

  // Smooth page transitions between internal pages
  if(!reduceMotion){
    document.addEventListener('click', function(e){
      var a = e.target.closest && e.target.closest('a[href]');
      if(!a) return;
      if(a.target === '_blank' || a.hasAttribute('download')) return;
      var href = a.getAttribute('href');
      if(!href || href.charAt(0)==='#' || href.indexOf('mailto:')===0 || href.indexOf('tel:')===0 || href.indexOf('http')===0) return;
      if(e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
      e.preventDefault();
      document.documentElement.classList.add('hv-pt-leave');
      setTimeout(function(){ location.href = href; }, 220);
    });
  }
})();
