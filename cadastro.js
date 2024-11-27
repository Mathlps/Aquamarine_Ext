// Conta permitida para acesso
const contaPermitida = {
    email: "admin@aquamarine.com",
    senha: "12345"
};

// Selecionar o formulário e os campos
const loginForm = document.getElementById("loginForm");
const emailInput = document.getElementById("email");
const senhaInput = document.getElementById("senha");

loginForm.addEventListener("submit", (event) => {
    event.preventDefault(); // Evita o envio do formulário

    const email = emailInput.value;
    const senha = senhaInput.value;

    // Validação da conta
    if (email === contaPermitida.email && senha === contaPermitida.senha) {
        alert("Login realizado com sucesso!");
        // Redirecionar para a página principal
        window.location.href = "geralAdministrador.html";
    } else {
        alert("E-mail ou senha incorretos. Tente novamente.");
    }
});
