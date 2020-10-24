import os
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/'
def fibonacci():
    resultado = "0.1."
    soma = None
    resultado1 = 1
    atual = [0, 1]
    indice = 0
    indice1 = 1
    while resultado1 < 50:
        soma = atual[indice] + atual[indice1]
        atual.append(soma)
        resultado += str(soma) + "."
        indice += 1
        indice1 += 1
        resultado1 += 1
    return resultado

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
