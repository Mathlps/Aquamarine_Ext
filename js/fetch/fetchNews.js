import config from '../config.js'; // importa a rota da API pre config
import { formatarData } from '../formatDate.js';

const apiUrl = config.API_URL;

const news = async () => {
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

const renderNews = (newsData) => {
    const newsContainer = document.querySelector('.noticias-main');
    newsContainer.innerHTML = ''; // Limpa o container antes de adicionar novas notícias

    let index = 1;
    newsData.forEach(news => {
        const dataFormatada = formatarData(news.data_publicacao); // Chamada correta da função
        const newsCard = `
            <a class="noticias-card" href="https://blog.sympla.com.br/guia-do-publico/o-que-e-o-projeto-tamar/">
                <div class="noticias-card-img">
                    <img src="https://blog.sympla.com.br/wp-content/uploads/2023/10/08-projeto-tamar.jpg" alt="">
                </div>

                <div class="noticias-card-content">
                    <h2>${news.titulo}</h2>
                    <p>${news.texto}</p>
                    <div class="noticias-card-data">${dataFormatada}</div>
                </div>
            </a>
        `;
        newsContainer.innerHTML += newsCard;
    });
    console.table(newsData)
}

const onNews = async () => {
    let project = await news()
    console.table(project); // Mostra os dados do projeto
    renderNews(project)
}

window.onload = onNews