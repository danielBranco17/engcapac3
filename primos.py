import os
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def primos():
    limite = 100

    b = 1
    n = 3

    primos = '2,'

    while b < limite:
        ehprimo = 1
        for i in range(2, n):
            if n % i == 0:
                ehprimo = 0
                break

        if(ehprimo):
            primos = primos + str(n) + '.'
            b += 1
            if(b % 10 == 0):
                primos = primos + '<br>'
        n += 1

    return primos

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
