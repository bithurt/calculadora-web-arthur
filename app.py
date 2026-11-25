from flask import Flask, jsonify, render_template, request
import operacoes

app = Flask(__name__)


def calcular_operacao(funcao):
    dados = request.get_json(silent=True) or {}

    try:
        valor1 = float(dados["valor1"])
        valor2 = float(dados["valor2"])
    except (KeyError, TypeError, ValueError):
        return jsonify({"erro": "Digite dois números válidos."}), 400

    try:
        resultado = funcao(valor1, valor2)
    except ZeroDivisionError:
        return jsonify({"erro": "Não é possível dividir por zero."}), 400

    return jsonify({"resultado": resultado})


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/soma")
def soma_page():
    return render_template("soma.html")


@app.route("/api/soma", methods=["POST"])
def soma():
    return calcular_operacao(operacoes.calcular_soma)


@app.route("/subtracao")
def subtracao_page():
    return render_template("subtracao.html")


@app.route("/api/subtracao", methods=["POST"])
def subtracao():
    return calcular_operacao(operacoes.calcular_subtracao)


@app.route("/multiplicacao")
def multiplicacao_page():
    return render_template("multiplicacao.html")


@app.route("/api/multiplicacao", methods=["POST"])
def multiplicacao():
    return calcular_operacao(operacoes.calcular_multiplicacao)


@app.route("/divisao")
def divisao_page():
    return render_template("divisao.html")


@app.route("/api/divisao", methods=["POST"])
def divisao():
    return calcular_operacao(operacoes.calcular_divisao)


if __name__ == "__main__":
    app.run(debug=True)
