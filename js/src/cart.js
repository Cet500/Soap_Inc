//
// Инициализирующий скрипт.
// Срабатывает на каждой странице, сразу же после её загрузки.
//
$(document).ready( function () {

	checkLS( "soap", [] )

	setSoapCost();

	array = $.localStorage( "soap" )
	array.forEach(function toggleButtons(el) {
		$('button[data-soap-id='+el[0]+']').toggleClass("hidden").prev().html("Взято ("+el[7]+")").toggleClass("hidden");
	})

});

//
// Срабатывает при нажатии на кнопку "купить" на странице каталога.
// Подменяет кнопку и записывает данные о товаре в LocalStorage.
//
function buySoap(el) {

	array = $.localStorage( "soap" )
	array.push([
		$(el).data("soapId"),    // 0
		$(el).data("soapType"),  // 1
		$(el).data("soapName"),  // 2
		$(el).data("soapPrice"), // 3
		$(el).data("soapColor"), // 4
		$(el).data("soapAroma"), // 5
		$(el).data("soapImage"), // 6
		/*soapCount*/ 1          // 7

	])
	$.localStorage( "soap", array )

	$(el).toggleClass("hidden");
	$(el).prev().toggleClass("hidden");

	setSoapCost();

}

//
// Проверяет, если такой элемент в LocalStorage.
// Если нет, то инициализирует его.
// Вызывается лишь раз при загрузке каждой страницы.
//
function checkLS(item, init_value) {

	if (localStorage.getItem(item) === null) {
		$.localStorage( item, init_value );
	}

}

//
// Посчитывает стоимость товаров, записанных в корзину ( LocalStorage ).
// Затем выводит эти данные на страницу.
// Вызывается при загрузке страницы, а также при каждом изменении корзины.
//
function setSoapCost() {

	array = $.localStorage( "soap" )

	var cart_value = 0;

	array.forEach(function summary(el) {
		cart_value += (el[3] * el[7]);
	})

	$(".scripts__soap-cost").html(cart_value);

}

//
// Уменьшает количество товара в коризине на единицу
//
function setLessSoap(el) {
	var temp = $(el).next().html();
	temp = Number(temp) - 1;
	$(el).next().html( temp );

	array = $.localStorage( "soap" )
	array.forEach(function toggleCount(arr) {
		if ( arr[0] === Number($(el).data("soapId")) ) {
			arr[7] = temp;
			console.log( temp )
		}
	})
	$.localStorage( "soap", array );

	setSoapCost();
}

//
// Увеличивает количество товара в коризине на единицу
//
function setMoreSoap(el) {
	var temp = $(el).prev().html();
	temp = Number(temp) + 1;
	$(el).prev().html( temp );

	array = $.localStorage( "soap" )
	array.forEach(function toggleCount(arr) {
		if ( arr[0] === Number($(el).data("soapId")) ) {
			arr[7] = temp;
		}
	})
	$.localStorage( "soap", array );

	setSoapCost();
}
