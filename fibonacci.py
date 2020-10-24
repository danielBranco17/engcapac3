import os
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def fibonacci():
    prox = 1
    ant = 0
    lim = 50
    found = 0
    resultado = "0,"
    while (found < lim):
        tmp = prox
        prox = prox + ant
        ant = tmp
        found = found + 1
        resultado += str(prox) + "."
    return resultado

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
