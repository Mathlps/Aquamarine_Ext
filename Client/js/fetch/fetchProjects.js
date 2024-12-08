import config from '../config.js'; // importa a rota da API pre config

const apiUrl = config.API_URL;

const projects = async () => {
    try {
        const response = await fetch(`${apiUrl}projetos`);
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json()
        return data // Retorna os dados em JSON
    } catch (error) {
        console.error('Houve um problema com a requisição Fetch:', error);
        return null // Caso haja um erro, retorna null
    }
}

const renderProjects = (json) => {
    const projects = json;
    const projectsContainer = document.querySelector('.content-container'); // Seleciona o container onde os projetos serão inseridos

    projectsContainer.innerHTML = ''; // Limpa o conteúdo anterior

    projects.forEach((project) => {
        // Usa o índice para acessar a imagem correspondente em img.images

        const delimitadores = ["Meta", "Como Funciona", "Parcerias e apoio"];
        const regex = new RegExp(`(?:${delimitadores.join('|')})`, 'g'); // (?:...) cria um grupo não capturador

        const partes = project.texto.split(regex).map(p => p.trim()).filter(p => p); // Remove strings vazias e espaços extras

        const projectCard = `
            <div class="content">
                <div class="content-title">
                    <h1 class="animate">${project.titulo}</h1>
                </div>
                <div class="content-items">
                    <div class="project-image">
                        <img class="animate" src="${project.link_imagem}" alt="${project.titulo}">
                    </div>
                    <div class="project-description">
                        <div class="text">
                            <h3 class="animte">Meta</h3>
                            <p class="animate">${partes[0]}</p>
                            <h3 class="animte">Como Funciona</h3>
                            <p class="animate">${partes[1]}</p>
                            <h3 class="animte">Parcerias e apoio</h3>
                            <p class="animate">${partes[2]}</p>
                            </div>
                        <div class="donation-button">
                            <a href="#" class="button animate">Junte-se a Nós</a>
                        </div>
                    </div>
                </div>
            </div>
        `;
        projectsContainer.innerHTML += projectCard; // Adiciona o card do projeto ao container
    });
};

const onProjects = async () => {
    let project = await projects()
    console.table(project) // Mostra os dados do projeto
    if (project !== null) renderProjects(project)
}

window.onload = onProjects