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

const animalsMain = async () => {
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
    console.table(project); // Mostra os dados
    let animals = await animalsMain()
    console.table(animals)
    let news = await newsMain()
    console.table(news)
}

onMain();