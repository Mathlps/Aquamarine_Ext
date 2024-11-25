// Função para carregar o conteúdo de um arquivo HTML
const loadHTML = (elementId, filePath) => {
    fetch(filePath)
        .then(response => response.text())
        .then(data => {
            document.getElementById(elementId).innerHTML = data;
        })
        .catch(error => console.error('Erro ao carregar o arquivo:', error));
}

// Executar ao carregar a página
document.addEventListener("DOMContentLoaded", () => {
    // Carregando a navbar e o footer
    loadHTML('header', 'navbar.html');
    loadHTML('footer', 'footer.html');
});