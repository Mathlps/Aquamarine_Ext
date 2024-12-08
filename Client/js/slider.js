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
const citacoes = document.querySelectorAll('.citacao');
const botaoAnterior = document.getElementById('anterior');
const botaoProximo = document.getElementById('proximo');
let indiceAtual = 0;
let temporizadorAutoSlide;

// Função para exibir a citação no índice dado com transições
function exibirCitacao(indice, direcao) {
  citacoes.forEach((citacao, i) => {
    citacao.classList.remove('ativa', 'sair-esquerda', 'sair-direita', 'entrar-esquerda', 'entrar-direita');
    
    if (i === indice) {
      citacao.classList.add('ativa');  // A citação no índice atual se torna visível
    } else if (i === (indiceAtual - 1 + citacoes.length) % citacoes.length) {
      citacao.classList.add('entrar-esquerda');  // Citação anterior (vindo da esquerda)
    } else if (i === (indiceAtual + 1) % citacoes.length) {
      citacao.classList.add('entrar-direita');  // Próxima citação (vindo da direita)
    } else if (direcao === 'anterior'){
      citacao.classList.add('sair-esquerda');
      // Outras citações sairão para a esquerda ou direita dependendo da direção
    } else if (direcao === 'proximo'){
      citacao.classList.add('sair-esquerda')
    }
  });
  indiceAtual = indice;  // Atualiza o índice atual para o novo índice da citação
}

// Função para iniciar/resetar o auto-slide
function iniciarAutoSlide() {
  clearInterval(temporizadorAutoSlide);
  temporizadorAutoSlide = setInterval(() => exibirCitacao((indiceAtual + 1) % citacoes.length, 'proximo'), 5000);
}

// Adicionando os ouvintes de evento para os botões de navegação
botaoAnterior.addEventListener('click', () => {
  exibirCitacao((indiceAtual - 1 + citacoes.length) % citacoes.length, 'anterior');
  iniciarAutoSlide();
});

botaoProximo.addEventListener('click', () => {
  exibirCitacao((indiceAtual + 1) % citacoes.length, 'proximo');
  iniciarAutoSlide();
});

// Inicializa o auto-slide ao carregar a página
iniciarAutoSlide();
