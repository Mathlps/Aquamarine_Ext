import config from '../config.js'; // importa a rota da API pre config
import { formatarData } from '../formatDate.js';

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
    }
}

const renderProjects = (json) => {
    const projects = json
    const projectsContainer = document.querySelector('.content-container'); // Seleciona o container onde os projetos serão inseridos

    projectsContainer.innerHTML = null

    projects.forEach(project => {
        const projectCard = `
            <div class="content">
                <div class="content-title">
                    <h1 class="animate">${project.titulo}</h1>
                </div>
                <div class="content-items">
                    <div class="project-image">
                        <img class="animate" src="img/projetos/projetos/projeto-praias-limpas.jpg" alt="exemplo">
                    </div>
                    <div class="project-description">
                        <div class="text">

                            <h3 class="animate">Meta</h3>
                            <p class="p1 animate">
                                O projeto "Praias Limpas" é uma iniciativa da ONG Aquamarine, que reúne voluntários
                                todos os meses em diversas praias ao longo da costa brasileira com o objetivo de
                                promover a limpeza das praias e a conscientização ambiental. O projeto surgiu da
                                necessidade urgente de combater a poluição dos oceanos, especialmente o acúmulo de
                                resíduos plásticos, que ameaçam a biodiversidade marinha e a saúde dos ecossistemas
                                costeiros.
                            </p>
                            <h3 class="animate">Como Funciona?</h3>
                            <p class="p2 animate">Todos os meses, equipes de voluntários se mobilizam para realizar
                                mutirões de limpeza
                                simultâneos em praias de várias regiões do Brasil. Desde o Norte até o Sul do país, as
                                ações são realizadas em locais previamente mapeados por apresentarem um acúmulo
                                significativo de lixo.
                            </p>
                            <p class="p3 animate">Durante os mutirões, também são realizadas atividades de
                                conscientização com os banhistas
                                e moradores locais, explicando o impacto do lixo nos oceanos e incentivando boas
                                práticas ambientais.
                            </p>
                            <h3 class="animate">Parcerias e apoio</h3>
                            <p class="p4 animate">O projeto conta com o apoio de voluntários, que dão o suporte
                                necessário para a
                                realização das ações.
                                Além disso, escolas e universidades também são envolvidas no projeto, realizando
                                campanhas educativas e incentivando os alunos a participarem dos mutirões como parte de
                                atividades extracurriculares focadas em cidadania e responsabilidade ambiental.</p>
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
}

const onProjects = async () => {
    let project = await projects()
    console.table(project); // Mostra os dados do projeto
    renderProjects(project)
}

window.onload = onProjects