// Publication filters: one active type and one active tag at a time.
document.addEventListener('DOMContentLoaded', function() {
  // The type button marked active in the HTML is the initial filter.
  var initial = document.querySelector('.tag-btn-type.tag-btn-active');
  var activeType = initial && initial.getAttribute('data-type') !== 'all'
    ? initial.getAttribute('data-type') : null;
  var activeTag = null;
  var typeButtons = document.querySelectorAll('.tag-btn[data-type]');
  var tagButtons = document.querySelectorAll('.tag-btn[data-tag]');
  var papers = document.querySelectorAll('.paper[data-tags]');
  var interests = document.querySelectorAll('.interest[data-tags]');

  function hasTag(el) {
    return !activeTag || el.getAttribute('data-tags').split(',').indexOf(activeTag) !== -1;
  }

  function apply() {
    papers.forEach(function(p) {
      var typeMatch = !activeType || p.getAttribute('data-type') === activeType;
      p.style.display = typeMatch && hasTag(p) ? '' : 'none';
    });
    interests.forEach(function(p) { p.style.display = hasTag(p) ? '' : 'none'; });
    typeButtons.forEach(function(b) {
      var type = b.getAttribute('data-type');
      b.classList.toggle('tag-btn-active', type === 'all' ? !activeType : type === activeType);
    });
    tagButtons.forEach(function(b) {
      var tag = b.getAttribute('data-tag');
      b.classList.toggle('tag-btn-active', tag === 'all' ? !activeTag : tag === activeTag);
    });
  }

  typeButtons.forEach(function(btn) {
    btn.addEventListener('click', function() {
      var type = this.getAttribute('data-type');
      activeType = type === 'all' || activeType === type ? null : type;
      apply();
    });
  });

  tagButtons.forEach(function(btn) {
    btn.addEventListener('click', function() {
      var tag = this.getAttribute('data-tag');
      activeTag = tag === 'all' || activeTag === tag ? null : tag;
      apply();
    });
  });
});
