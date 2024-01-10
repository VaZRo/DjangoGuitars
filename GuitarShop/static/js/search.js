$(document).ready(function() {
  $("#find_field").keydown(function(e) {
    if (e.keyCode == 13) {
      var name = $("#find_field").val();
      console.log(name);

      class Find{
        constructor(name, price, img){
          this._name = name;
          this._price = price;
          this._img = img;
      }
      get name(){
          return this._name;
      }
      get price(){
          return this._price;
      }
      get img(){
          return this._img;
      }
      }

      var finds = [];

      // создание модального окна

      $('#search-menu').modal({
        escapeClose: true,
        clickClose: true,
        showClose: true,
        fadeDuration: 300,
        fadeDelay: 0.5
      });

      // поиск элементов

      var models = $(".model");
    
      for(var i = 0; i < models.length; i++){
        var once = false;
        var onceName = models.eq(i).find(".name").text();
        for(j = 0; j < name.length; j++){
          if(onceName[j] != name[j]){
            once = true;
            break;
          }
        }

        if(once == false){
          var nameGuitar = models.eq(i).find(".name").text();
          var price = models.eq(i).find(".price").text();
          var src = models.eq(i).find(".guitar").attr("src");

          $(".cart-menu .modal-body").append("<div class=\"pos\"><div class=\"pos-left\"><div class=\"ava-div\"><img src=\"" + src + "\" class=\"ava\"/></div><div class=\"pos-text\"><div>Name: " + nameGuitar + "</div><div>Price: " + price + "</div></div></div><div class=\"pos-delete\"><i class=\"fa-solid fa-trash fa-2xl\" style=\"color: #000000;\"></i></div></div>");       
                i++;
                $(".cart-menu .modal-button").removeClass("invisible");
          }
        }
      }
	});
});
