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