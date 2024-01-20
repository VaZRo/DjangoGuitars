window.onload = function(){
    $('.basket_list').on('click', 'input[type="number"]', function(ev){
        let t_href = ev.target;

        $.ajax({
            url: '/basket/edit/' + t_href.name + '/' + t_href.value + '/',
            success: function (data){
                $('.basket_list').html(data.result);
            }
        })

        ev.preventDefault();
    })
}