// HEADER SCROLL ANIMATION
window.addEventListener("scroll", function () {
    let header = document.querySelector('#header')
    header.classList.toggle('rolagem', window.scrollY > 0)
})

const hambuguer = document.querySelector(".hambuguer")
const nav = document.querySelector(".nav")

hambuguer.addEventListener("click", () => nav.classList.toggle("active"))