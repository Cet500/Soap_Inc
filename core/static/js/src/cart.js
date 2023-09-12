//
// Инициализирующий скрипт.
// Срабатывает на каждой странице, сразу же после её загрузки.
//
$(document).ready( function () {

	checkLS( "soap", [] )

	setSoapCost();

	array = $.localStorage( "soap" )
	array.forEach(function toggleButtons(el) {
		$('button[data-soap-id=' + el[0] + ']').toggleClass("hidden")
			.prev().html("Взято (" + el[7] + ")").toggleClass("hidden");
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
function checkLS(ls_item, ls_init_value) {

	if (localStorage.getItem(ls_item) === null) {
		$.localStorage( ls_item, ls_init_value );
	}

}

//
// Посчитывает стоимость товаров, записанных в корзину (LocalStorage).
// Затем выводит эти данные на страницу.
// Вызывается при загрузке страницы, а также при каждом изменении корзины.
//
function setSoapCost() {

	ls_soap = $.localStorage( "soap" )

	let cart_value = 0;

	ls_soap.forEach(function summary(el) {
		cart_value += (el[3] * el[7]);
	})

	$(".scripts__soap-cost").html(cart_value);

}

//
// Уменьшает количество товара в корзине на единицу
//
function setLessSoap(el) {

	let ls_soap = $.localStorage( "soap" );
	let soap_id = Number($(el).data("soapId") );
	let value = Number( $(el).next().html() );
	value = value - 1;

	if ( value <= 0 ) {

		for (let i = 0; i < ls_soap.length; i++) {
			if ( ls_soap[i][0] === soap_id ) {
				ls_soap.splice(i, 1);
			}
		}

		$(el).parent().parent().remove();

	}
	else {

		ls_soap.forEach(function (arr) {
			if ( arr[0] === soap_id ) {
				arr[7] = value;
			}
		})

		$(el).next().html( value );

	}

	$.localStorage( "soap", ls_soap );

	setSoapCost();

}

//
// Увеличивает количество товара в корзине на единицу
//
function setMoreSoap(el) {

	let ls_soap = $.localStorage( "soap" );
	let soap_id = Number($(el).data("soapId") );
	let value = Number( $(el).prev().html() );
	value = value + 1;

	ls_soap.forEach(function (arr) {
		if ( arr[0] === soap_id ) {
			arr[7] = value;
		}
	})

	$(el).prev().html( value );

	$.localStorage( "soap", ls_soap );

	setSoapCost();


}
