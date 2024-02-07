$(document).ready(function() {
    $('.modal-body').on('click', 'input[type="number"]', function(ev){
        let t_href = ev.target;
        console.log(t_href);
        $.ajax({
            url: '/basket/edit/' + t_href.name + '/' + t_href.value + '/',
            success: function (data){
                $('.modal-body').html(data.result);
            }
        })

        ev.preventDefault();
    })

        $('.model').on('click', '.buy', function(ev){
        let t_href = ev.target
        $.ajax({
            url: '/basket/add/' + t_href.id + '/',
            success: function (data){
                console.log(data.result);
                $('.modal-body').html(data.result);
            }
        })

        ev.preventDefault();
    })

}