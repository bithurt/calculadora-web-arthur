function calcular(url) {
    const valor1 = document.getElementById("valor1").value;
    const valor2 = document.getElementById("valor2").value;
    const resultado = document.getElementById("resultado");

    if (valor1 === "" || valor2 === "") {
        resultado.innerText = "Digite os dois valores.";
        return;
    }

    fetch(url, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ valor1: valor1, valor2: valor2 })
    })
    .then(resposta => resposta.json().then(dados => ({ resposta, dados })))
    .then(({ resposta, dados }) => {
        if (!resposta.ok) {
            resultado.innerText = dados.erro;
            return;
        }

        resultado.innerText = "Resultado: " + dados.resultado;
    })
    .catch(() => {
        resultado.innerText = "Não foi possível fazer o cálculo.";
    });
}

function calcularSoma() {
    calcular("/api/soma");
}

function calcularSubtracao() {
    calcular("/api/subtracao");
}

function calcularMultiplicacao() {
    calcular("/api/multiplicacao");
}

function calcularDivisao() {
    calcular("/api/divisao");
}
