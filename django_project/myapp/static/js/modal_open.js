const openPopUp = document.getElementById('open')
const closePopUp = document.getElementById('pop_up_close')
const popUp = document.getElementById('pop_up')

openPopUp.addEventListener('click', function(e){
    e.preventDefault();
    popUp.classList.add('active')
})
closePopUp.addEventListener('click', () => {
    popUp.classList.remove('active')
})

const open1PopUp = document.getElementById('open1')
const close1PopUp = document.getElementById('pop_up_close1')
const popUp1 = document.getElementById('pop_up1')

open1PopUp.addEventListener('click', function(e){
    e.preventDefault();
    popUp1.classList.add('active')
})
close1PopUp.addEventListener('click', () => {
    popUp1.classList.remove('active')
})