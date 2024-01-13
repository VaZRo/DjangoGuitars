$(document).ready(function() {
        $('.toggle-button').click(function(event) {
            var filterSection = $(this).closest('.filter-section');
            var filterOptions = filterSection.find('.filter-options');

            filterOptions.toggleClass('active');
        });
    });