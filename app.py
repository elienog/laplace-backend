from flask import Flask, request, jsonify
from sympy import symbols, laplace_transform, simplify
from sympy.abc import t, s

app = Flask(__name__)

@app.route("/laplace", methods=["POST"])
def calcular_laplace():
    try:
        data = request.get_json()
        expr_str = data.get("expression")

        if not expr_str:
            return jsonify({"error": "No se proporcionó una función."}), 400

        expr = simplify(expr_str)
        F = laplace_transform(expr, t, s, noconds=True)

        return jsonify({"result": str(F)})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/", methods=["GET"])
def home():
    return "API de Transformada de Laplace activa."
