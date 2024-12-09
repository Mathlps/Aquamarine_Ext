const contaPermitida = {
    email: "admin@aquamarine.com.br",
    senha: "12345"
};

const loginForm = document.getElementById("loginForm");
const emailInput = document.getElementById("email");
const senhaInput = document.getElementById("senha");

loginForm.addEventListener("submit", (event) => {
    event.preventDefault();

    const email = emailInput.value;
    const senha = senhaInput.value;

    if (email === contaPermitida.email && senha === contaPermitida.senha) {
        alert("Login realizado com sucesso!");
        window.location.href = "geralAdministrador.html";
    } else {
        alert("E-mail ou senha incorretos. Tente novamente.");
    }
});

// import config from 'config'; // Importa o config.js

// const loginForm = document.getElementById("loginForm");
// const emailInput = document.getElementById("email");
// const senhaInput = document.getElementById("senha");

// loginForm.addEventListener("submit", async (event) => {
//     event.preventDefault();

//     const email = emailInput.value;
//     const senha = senhaInput.value;

//     alert(email + "\n" + senha)

//     // Enviar requisição para o backend usando a API_URL do config
//     const response = await fetch(`${config.API_URL}login`, { // Usa a API_URL
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         body: JSON.stringify({ email, senha })
//     });

//     const data = await response.json();

//     if (response.ok) {
//         alert("Login realizado com sucesso!");
//         window.location.href = "geralAdministrador.html"; // Redireciona para a página do administrador
//     } else {
//         alert(data.error || "E-mail ou senha incorretos. Tente novamente.");
//     }
// });