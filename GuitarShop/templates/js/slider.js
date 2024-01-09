// Слайд

$(document).ready(function() {
    var slides = $(".slide");
    slides[0].classList.add("active");
    var numberOfSlide = 0;
    
    setInterval(function(){
    slides.eq(numberOfSlide).removeClass("active");
    numberOfSlide = (numberOfSlide + 1) % slides.length;
    slides.eq(numberOfSlide).addClass("active");
    }, 5000)

    $(".shop-button").click(function(){
        $("html").animate({
            scrollTop: $(".metal").offset().top
          }, 1000);
    })
})


