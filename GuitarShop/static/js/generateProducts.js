$(document).ready(function () {
    // Получаем CSRF-токен
    let csrftoken = $("[name=csrfmiddlewaretoken]").val();

    let filterData = {}

    getProduct();

    $('.apply-button').click(filterProduct);

    $('.clear-button').click(function () {
        $('#filterForm input[type="checkbox"]').prop('checked', false);
        filterData = {};
        getProduct();
    });

    function filterProduct() {
        filterData = {};  // Обновляем объект перед каждым применением фильтра
        $('input[type="checkbox"]:checked').each(function () {
            let filterName = $(this).attr('name').split('-')[0];
            let filterId = $(this).attr('name').split('-')[1];
            if (filterData.hasOwnProperty(filterName)) {
                // Создаем Set, если его еще нет, и добавляем filterId
                filterData[filterName].add(filterId);
            } else {
                // Если ключа нет, создаем новый Set с этим значением
                filterData[filterName] = new Set([filterId]);
            }
        });

        // Преобразуем множество в массив
        Object.keys(filterData).forEach(function (key) {
            filterData[key] = Array.from(filterData[key]);
        });
        getProduct();
    }


    function getProduct() {
        // При загрузке страницы делаем AJAX-запрос
        $.ajax({
            url: '/products/get-products/',
            type: 'POST',
            data: JSON.stringify({
                filterData: filterData
            }),
            contentType: 'application/json',
            dataType: 'json',
            beforeSend: function (xhr) {
                // Устанавлива  ем заголовок с CSRF-токеном
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            },
            success: function (data) {
                // Обработка успешного ответа
                renderProducts(data);
                // console.log(data);
            },
            error: function (error) {
                console.error('Error fetching data:', error);
            }
        });
        console.log("Sent filterData:", filterData);
    }

    // Функция для отображения продуктов
    function renderProducts(products) {
        let productContainer = $('#product-container');

        // Очищаем контейнер перед добавлением новых продуктов
        productContainer.empty();

        // Генерируем HTML-код для каждого продукта
        $.each(products, function (index, prod) {
            let productHtml = `
                <div class="model" id="${prod.pk}">
                    <div class="all">
                    <a href="${prod.url}"><img class="guitar" src="${prod.image}" alt="${prod.name}"></a>
                        <div class="info">
                            <div class="name">${prod.name}</div>
                            <div class="line"></div>
                            <div class="price">${prod.price} $</div>
                            <div class="buy" id="${prod.pk}" onclick="addToCart(event)">Add To Cart</div>
                        </div>
                    </div>
                </div>
            `;

            // Добавляем HTML-код продукта в контейнер
            productContainer.append(productHtml);
        });
    }
});

