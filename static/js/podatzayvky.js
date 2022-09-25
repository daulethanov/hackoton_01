let burgerMenuButton = document.querySelector('.burger__menu__button');
let burgerContent = document.querySelector('.burger__content')
burgerMenuButton.addEventListener('click', function () {
	burgerMenuButton.classList.toggle('burger__menu__button__active');
	burgerContent.classList.toggle('burger__content__active');
});

// вход
let vhodIcon = document.querySelector('.vhod__icon');
let vhodPosition = document.querySelector('.vhod__position');
vhodIcon.addEventListener('click', function () {
	vhodPosition.classList.toggle('vhod__position__active');
});

// регестрация
let registrSpam = document.querySelector('.registr__spam ');
let registrPosition = document.querySelector('.registr__position');
registrSpam.addEventListener('click', function () {
	registrPosition.classList.toggle('registr__position__active');
	vhodPosition.classList.remove('vhod__position__active');
});