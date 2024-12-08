import config from '../config.js'; // importa a rota da API pre config
import { formatarData } from '../formatDate.js';

const apiUrl = config.API_URL;

const newsFunc = async () => {
    try {
        const response = await fetch(`${apiUrl}noticias`);
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json()
        return data // Retorna os dados em JSON
    } catch (error) {
        console.error('Houve um problema com a requisição Fetch:', error);
        return null
    }
}

const renderNews = (newsData) => {
    const newsContainer = document.querySelector('.noticias-main');
    newsContainer.innerHTML = ''; // Limpa o container antes de adicionar novas notícias

    let index = 1;
    newsData.forEach(news => {
        const dataFormatada = formatarData(news.data_publicacao); // Chamada correta da função
        const newsCard = `
            <a class="noticias-card" href="${news.link_noticia}">
                <div class="noticias-card-img">
                    <img src="${news.link_imagem}" alt="">
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
    let news = await newsFunc()
    console.table(news); // Mostra os dados do projeto
    if(news !== null) renderNews(news)
}

window.onload = onNews