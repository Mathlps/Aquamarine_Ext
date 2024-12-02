import config from './config.js'; // importa a rota da API pre config

const apiUrl = config.API_URL;

const projectsMain = async () => {
    try {
        const response = await fetch(`${apiUrl}projetos`);
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json()
        return data // Retorna os dados em JSON
    } catch (error) {
        console.error('Houve um problema com a requisição Fetch:', error);
    }
}

const renderProjects = (json) => {
    const projects = json
    const projectsContainer = document.querySelector('.projetos'); // Seleciona o container onde os projetos serão inseridos

    projectsContainer.innerHTML = null

    projects.forEach(project => {
        const projectCard = `
            <div class="card animate">
                <div class="card-inner">
                    <div class="card-front-${project.id}">
                        <h3>${project.titulo}</h3> <!-- Substitui pelo título do projeto -->
                    </div>
                    <div class="card-back">
                        <p>${project.texto}</p> <!-- Substitui pela descrição do projeto -->
                        <button onclick="location.href='projetos.html?id=${project.id}'">SAIBA MAIS</button> <!-- Link para a página de detalhes do projeto -->
                    </div>
                </div>
            </div>
        `;
        projectsContainer.innerHTML += projectCard; // Adiciona o card do projeto ao container
    });
}

const animalsMain = async () => {
    try {
        const response = await fetch(`${apiUrl}animais`);
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json()
        return data // Retorna os dados em JSON
    } catch (error) {
        console.error('Houve um problema com a requisição Fetch:', error);
    }
}

// const renderAnimals = 

const newsMain = async () => {
    try {
        const response = await fetch(`${apiUrl}noticias`);
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json()
        return data // Retorna os dados em JSON
    } catch (error) {
        console.error('Houve um problema com a requisição Fetch:', error);
    }
}

const onMain = async () => {
    let project = await projectsMain()
    console.table(project); // Mostra os dados do projeto
    renderProjects(project)

    let animals = await animalsMain()
    console.table(animals) // Mostra os dados dos animais
    renderAnimals(animals)

    let news = await newsMain()
    console.table(news) // Mostra os dados das noticias
}

onMain();