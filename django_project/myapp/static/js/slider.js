
var slide_1 = document.getElementById("slide-1");
var slide_2 = document.getElementById("slide-2");
var slide_3 = document.getElementById("slide-3");

var slide_button_1 = document.querySelector(".product-1");
var slide_button_2 = document.querySelector(".product-2");
var slide_button_3 = document.querySelector(".product-3");

slide_1.addEventListener("click", function (evt) {
  document.body.style.backgroundColor = '#849d8f';
  document.getElementById("slide1").classList.remove("visually-hidden");
  document.getElementById("slide2").classList.add("visually-hidden");
  document.getElementById("slide3").classList.add("visually-hidden");
  slide_button_1.style.backgroundColor = 'white';
  slide_button_2.style.backgroundColor = 'transparent';
  slide_button_3.style.backgroundColor = 'transparent';
});

slide_2.addEventListener("click", function (evt) {
  document.body.style.backgroundColor = '#8996a6';
  document.getElementById("slide1").classList.add("visually-hidden");
  document.getElementById("slide2").classList.remove("visually-hidden");
  document.getElementById("slide3").classList.add("visually-hidden");
  slide_button_1.style.backgroundColor = 'transparent';
  slide_button_2.style.backgroundColor = 'white';
  slide_button_3.style.backgroundColor = 'transparent';
});

slide_3.addEventListener("click", function (evt) {
  document.body.style.backgroundColor = '#9d8b84';
  document.getElementById("slide1").classList.add("visually-hidden");
  document.getElementById("slide2").classList.add("visually-hidden");
  document.getElementById("slide3").classList.remove("visually-hidden");
  slide_button_1.style.backgroundColor = 'transparent';
  slide_button_2.style.backgroundColor = 'transparent';
  slide_button_3.style.backgroundColor = 'white';
});
