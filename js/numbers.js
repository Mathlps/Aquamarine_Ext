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