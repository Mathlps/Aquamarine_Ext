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

// ANIMAÇÃO OPACIDADE DE BOTÃO VOLTAR AO TOPO

var btn = document.querySelector('.voltar-ao-topo'); // pega itens com classe voltar-ao-topo

window.addEventListener('scroll', function() {
  if (window.scrollY > 500) {
    btn.classList.add('mostrar'); // adiciona visibilidade se for maior que 700 de altura da página
  } else {
    btn.classList.remove('mostrar'); 
  }
});
