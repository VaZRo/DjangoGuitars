function addToCart(ev){
        let t_href = ev.target
        $.ajax({
            url: '/basket/add/' + t_href.id + '/',
            success: function (data){
                console.log(data.result);
                $('.modal-body').html(data.result);
            }
        })

        ev.preventDefault();
    }

function deleteFromCart(ev){
    let t_href = ev.target
        $.ajax({
            url: '/basket/remove/' + t_href.id + '/',
            success: function (data){
                console.log(data.result);
                $('.modal-body').html(data.result);
            }
        })

        ev.preventDefault();
}
