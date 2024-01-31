$(document).ready(function() {

    $(".buy").click(function(){
        var parent = $(this).parent();
        var name = parent.find(".name").text();
        var price = parent.find(".price").text();
        var src = parent.parent().find(".guitar").attr("src");
        carts.push(new Cart(name, price, src));
        $(".cart-menu .modal-body").append("<div class=\"pos\"><div class=\"pos-left\"><div class=\"ava-div\"><img src=\"" + carts[i].img + "\" class=\"ava\"/></div><div class=\"pos-text\"><div>Name: " + carts[i].name + "</div><div>Price: " + carts[i].price + "</div></div></div><div class=\"pos-delete\"><i class=\"fa-solid fa-trash fa-2xl\" style=\"color: #000000;\"></i></div></div>");
        i++;
        $(".cart-menu .modal-button").removeClass("invisible");
    });

    $(".cart").click(function(){
        // if(carts.length == 0){
        //     $(".modal-empty").text("Shopping Cart Is Empty");
        //     $(".cart-menu .modal-button").addClass("invisible");
        // }

        $('#cart-menu').modal({
            escapeClose: true,
            clickClose: true,
            showClose: true,
            fadeDuration: 300,
            fadeDelay: 0.5
          });
    });

    $("#cart-menu").on("click", ".pos-delete", function Delete() {
        carts.splice($(this).index(), 1);
        i--;
        if(i == 0){
            carts = [];
        }
        $(this).parent().remove();
        if(carts.length == 0){
            $(".modal-empty").text("Shopping Cart Is Empty");
            $(".cart-menu .modal-button").addClass("invisible");
        }
    });

    $("#cart-menu").on("click", ".modal-button", function() {
        $('#cart-buy').modal({
            escapeClose: true,
            clickClose: true,
            showClose: true,
            fadeDuration: 300,
            fadeDelay: 0.5
        });
        $(".modal-pos").text("You would buy " + carts.length + " position");
        $(".modal-price").text("Total price: " + FindingTotalPrice() + "$");
    });

    $("#cart-buy").on("click", ".modal-button", function() {

        $("#name-error, #surname-error, #address-error, #email-error, #number-error").text("");
        var pass = true;

        var name = $("#name").val();
        const nameRegex = /^[a-zA-Z]{2,}$/;
        if(!nameRegex.test(name)){
            $("#name-error").text("Invalid first name(2 and more letters)");
            pass = false;
        }

        var surname = $("#surname").val();
        if(!nameRegex.test(surname)){
            $("#surname-error").text("Invalid last name(2 and more letters)");
            pass = false;
        }

        var address = $("#address").val();
        const addressRegex = /^\w{8,}$/;
        if(!addressRegex.test(address)){
            $("#address-error").text("Invalid addres(8 and more letters)");
            pass = false;
        }

        var email = $("#email").val();
        const emailRegex = /^[^\s@]{3,15}@[^\s@]{2,}\.[^\s@]{2,}$/;
        if(!emailRegex.test(email)){
            $("#email-error").text("Invalid email");
            pass = false;
        }

        var number = $("#number").val();
        const numberRegex = /^\d{11}$/;
        if(!numberRegex.test(number)){
            $("#number-error").text("Invalid Number");
            pass = false;
        }

        if(pass == true){
            $(".pos").remove();
            carts = [];
            alert("Вы успешно совершили покупку");
        }
    });
});
