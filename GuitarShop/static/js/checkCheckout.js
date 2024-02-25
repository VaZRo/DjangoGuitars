    document.addEventListener('DOMContentLoaded', function () {
        document.getElementById('contact').addEventListener('submit', function (event) {
            var cardNumberInput = document.getElementById('cardNumber').value;
            var cardDateInput = document.getElementById('cardDate').value;
            var cardCVVInput = document.getElementById('cardCVV').value;

            var cardNumberPattern = /^\d{16}$/;
            var datePattern = /^(0[1-9]|1[0-2])\/\d{2}$/;
            var cvvPattern = /^\d{3}$/;

            if (!cardNumberPattern.test(cardNumberInput)) {
                alert('Номер карты должен содержать ровно 16 цифр');
                event.preventDefault();
            }

            if (!datePattern.test(cardDateInput)) {
                alert('Введите дату в формате MM/YY');
                event.preventDefault();
            }

            if (!cvvPattern.test(cardCVVInput)) {
                alert('CVV должен содержать ровно 3 цифры');
                event.preventDefault();
            }
        });
    });