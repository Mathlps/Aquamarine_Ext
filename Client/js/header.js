// HEADER SCROLL ANIMATION
window.addEventListener("scroll", function () {
    let header = document.querySelector('#header')
    header.classList.toggle('rolagem', window.scrollY > 0)
})

const hamburger = document.querySelector(".hamburger")

hamburger.addEventListener("click", () => {
    document.querySelector(".nav").classList.toggle("active")
})