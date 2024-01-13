$(document).ready(function () {
    $('.toggle-button').click(function (event) {
        let filterSection = $(this).closest('.filter-section');
        let filterOptions = filterSection.find('.filter-options');
        let showIcon = filterSection.find('.show-icon');

        filterOptions.toggleClass('active');
        if (showIcon.hasClass('ri-add-line')) {
            showIcon.removeClass('ri-add-line').addClass('ri-subtract-line');
        } else {
            showIcon.removeClass('ri-subtract-line').addClass('ri-add-line');
        }
    });

    $('.close-icon').click(function (event) {
        let filterMobile = $(this).closest('.filters-mobile');
        filterMobile.removeClass('active');
    });

    $('.mobile-filter-button').click(function (event) {
        let filterMobile = $('.main_page').find('.filters-mobile');
        console.log('Clicked on mobile-filter-button');
        console.log('Filter Mobile:', filterMobile.length);
        filterMobile.addClass('active');
    });
});