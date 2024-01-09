$(document).ready(function() {
    $(".metal .guitars.slider").slick({
        prevArrow: $(".metal .button-left"),
        nextArrow: $(".metal .button-right"),
        dots: false,
        infinite: true,
        speed: 500,
        slidesToShow: 3,
        slidesToScroll: 2,
        autoplay: true,
        autoplaySpeed: 5000,
        cssEase: 'ease-in-out',
      });

      $(".classic .guitars.slider").slick({
        prevArrow: $(".classic .button-left"),
        nextArrow: $(".classic .button-right"),
        dots: false,
        infinite: true,
        speed: 500,
        slidesToShow: 3,
        slidesToScroll: 2,
        autoplay: true,
        autoplaySpeed: 5000,
        cssEase: 'ease-in-out',
      });

      $(".stomps .guitars.slider").slick({
        prevArrow: $(".stomps .button-left"),
        nextArrow: $(".stomps .button-right"),
        dots: false,
        infinite: true,
        speed: 500,
        slidesToShow: 3,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 5000,
        cssEase: 'ease-in-out',
      });
})
