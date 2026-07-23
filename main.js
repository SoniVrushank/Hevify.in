(function(){
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  window.addEventListener('load', function(){
    setTimeout(function(){
      document.getElementById('preloader').classList.add('done');
    }, 500);
  });

  var nav = document.getElementById('siteNav');
  window.addEventListener('scroll', function(){
    nav.classList.toggle('scrolled', window.scrollY > 40);
  }, { passive: true });

  var words = ['Brands.', 'Campaigns.', 'Growth.', 'Movements.'];
  var wi = 0;
  var wordEl = document.getElementById('cycleWord');
  if (wordEl && !reduce) {
    setInterval(function(){
      wordEl.style.opacity = 0;
      setTimeout(function(){
        wi = (wi + 1) % words.length;
        wordEl.textContent = words[wi];
        wordEl.style.opacity = 1;
      }, 300);
    }, 2200);
  }

  if (window.gsap) {
    gsap.registerPlugin(ScrollTrigger);
    if (!reduce) {
      gsap.utils.toArray('.reveal').forEach(function(el){
        gsap.to(el, { opacity: 1, y: 0, duration: .8, ease: 'power3.out',
          scrollTrigger: { trigger: el, start: 'top 88%' } });
        gsap.set(el, { y: 26 });
      });
    } else {
      gsap.set('.reveal', { opacity: 1 });
    }

    document.querySelectorAll('.count').forEach(function(el){
      var target = +el.dataset.count;
      if (reduce) { el.textContent = target; return; }
      gsap.to(el, { textContent: target, duration: 1.6, ease: 'power2.out', snap: { textContent: 1 },
        scrollTrigger: { trigger: el, start: 'top 90%' } });
    });
    document.querySelectorAll('.count-decimal').forEach(function(el){
      var target = +el.dataset.count;
      if (reduce) { el.textContent = target.toFixed(1); return; }
      var obj = { val: 0 };
      gsap.to(obj, { val: target, duration: 1.6, ease: 'power2.out',
        onUpdate: function(){ el.textContent = obj.val.toFixed(1); },
        scrollTrigger: { trigger: el, start: 'top 90%' } });
    });
  } else {
    document.querySelectorAll('.reveal').forEach(function(el){ el.style.opacity = 1; });
  }
})();