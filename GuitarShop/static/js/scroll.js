$(document).ready(function () {
    $(".carousel .guitars.slider").slick({
        prevArrow: $(".carousel .button-left"),
        nextArrow: $(".carousel .button-right"),
        dots: false,
        infinite: true,
        slidesToShow: 3,
        slidesToScroll: 3,
        speed: 500,
        autoplay: true,
        autoplaySpeed: 5000,
        cssEase: 'ease-in-out',
        responsive: [
            {
                breakpoint: 1024,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 2,
                }
            },
            {
                breakpoint: 600,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1,
                }
            },
        ]
    });
})
