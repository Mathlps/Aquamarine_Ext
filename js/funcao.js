// HEADER SCROLL ANIMATION
window.addEventListener("scroll", function () {
    let header = document.querySelector('#header')
    header.classList.toggle('rolagem', window.scrollY > 0)
})

// SLIDER START
let slider = document.querySelector('.slider .list');
let items = document.querySelectorAll('.slider .list .item');
let next = document.getElementById('next');
let prev = document.getElementById('prev');
let dots = document.querySelectorAll('.slider .dots li');

let lengthItems = items.length - 1;
let active = 0;
next.onclick = function () {
    active = active + 1 <= lengthItems ? active + 1 : 0;
    reloadSlider();
}
prev.onclick = function () {
    active = active - 1 >= 0 ? active - 1 : lengthItems;
    reloadSlider();
}
let refreshInterval = setInterval(() => { next.click() }, 3000);
function reloadSlider() {
    slider.style.left = -items[active].offsetLeft + 'px';
    // 
    let last_active_dot = document.querySelector('.slider .dots li.active');
    last_active_dot.classList.remove('active');
    dots[active].classList.add('active');

    clearInterval(refreshInterval);
    refreshInterval = setInterval(() => { next.click() }, 3000);
}

dots.forEach((li, key) => {
    li.addEventListener('click', () => {
        active = key;
        reloadSlider();
    })
})
window.onresize = function (event) {
    reloadSlider();
};
// SLIDER END

// NUMEROS IMPACTADOS ANIMATION

let valueDisplays = document.querySelectorAll(".num");
let interval = 5000;

document.addEventListener("DOMContentLoaded", () => {        

    // Seleciona todos os elementos com a classe 'value-display' para a contagem
    const valueDisplays = document.querySelectorAll(".value-display");
    const interval = 1500; // Define um intervalo total para a contagem (em milissegundos)

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                valueDisplays.forEach((valueDisplay) => {
                    let startValue = 0;
                    let endValue = parseInt(valueDisplay.getAttribute("data-val"));
                    
                    // Verifica se endValue é um número válido
                    if (isNaN(endValue) || endValue <= 0) {
                        console.error("Atributo data-val inválido:", endValue);
                        return;
                    }

                    let duration = Math.floor(interval / endValue);
                    
                    let counter = setInterval(function () {
                        startValue += 1;
                        valueDisplay.textContent = startValue;
                        if (startValue === endValue) {
                            clearInterval(counter);
                        }
                    }, duration);
                });

                // Para observar o elemento apenas uma vez e não reiniciar a contagem
                observer.unobserve(entry.target);
            }
        });
    });

    // Observa cada elemento de contagem para ativar a animação ao aparecer na tela
    valueDisplays.forEach((element) => observer.observe(element));
});



// codigo para animar os elementos quando aparecem na tela

//animacao so acontece quando o elemento entra no viewport da tela

document.addEventListener("DOMContentLoaded", () => {         //checa se o documento carregou

    const observer = new IntersectionObserver(entries => {       //usa IntersectionObserver para ver se o elemento esta no viewport
      entries.forEach(entry => {
        if(entry.isIntersecting){
          entry.target.classList.add('in-view');
          return;
        }
        
      })
    })
  
    const allAnimatedElements = document.querySelectorAll('.animate');       //pega todos os elementos com .animate aplicados
  
    allAnimatedElements.forEach((element) => observer.observe(element));      //adiciona o observer para todos esses elementos
  
  })