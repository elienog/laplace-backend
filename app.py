from flask import Flask, request, jsonify
from sympy import symbols, laplace_transform, sympify, init_printing
from sympy.abc import t, s

app = Flask(__name__)
init_printing(use_unicode=True)

@app.route("/laplace", methods=["POST"])
def calcular_laplace():
    try:
        data = request.json
        funcion = sympify(data["funcion"])
        transformada, _, _ = laplace_transform(funcion, t, s)
        return jsonify({
            "input": str(funcion),
            "laplace": str(transformada)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run()
