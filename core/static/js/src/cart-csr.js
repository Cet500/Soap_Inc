//
// Инициализирующий скрипт.
// Срабатывает на странице корзины.
// Генерирует содержимое корзины на стороне клиента.
//
$(document).ready( function () {

	var tmpl = $.templates("#script__cart-template");
	var data = []

	array.forEach(function toggleButtons(el) {
		data.push({
			'id': el[0],
			'name': el[2],
			'price': el[3],
			'color': el[4],
			'aroma': el[5],
			'image': el[6],
			'count': el[7]
		})
	})

	var html = tmpl.render(data);
	$("#script__cart").html(html);

});
