function filter(e) {
	const animals = document.querySelectorAll(".section__filter div"); // select all animal divs
	let filter = e.target.dataset.filter; // grab the value in the event target's data-filter attribute

	if (filter === '*') {
		animals.forEach(animal => animal.classList.remove('hidden'));
	}
	else{
		animals.forEach(animal => {
			animal.classList.contains(filter) // does the animal have the filter in its class list?
				? animal.classList.remove('hidden') // if yes, make sure .hidden is not applied
				: animal.classList.add('hidden'); // if no, apply .hidden
		});
	}
};