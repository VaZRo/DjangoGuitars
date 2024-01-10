$(window).scroll(function() {
  if ($(this).scrollTop() > 0) {
    $('.menu').addClass('sticky');
  } else {
    $('.menu').removeClass('sticky');
  }
});
