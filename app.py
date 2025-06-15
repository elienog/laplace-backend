from flask import Flask, request, jsonify
from sympy import symbols, laplace_transform, sympify, simplify
from sympy.abc import t, s

app = Flask(__name__)

@app.route('/laplace', methods=['POST'])
def laplace_api():
    data = request.get_json()
    try:
        expr = sympify(data['function'])
        L, _, _ = laplace_transform(expr, t, s)
        return jsonify({
            "original": str(expr),
            "laplace": str(simplify(L))
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/', methods=['GET'])
def home():
    return 'API de Transformada de Laplace funcionando.'
