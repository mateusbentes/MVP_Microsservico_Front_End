from flask import Flask, request, Response, jsonify, redirect
from flask_cors import CORS
import requests

app = Flask(__name__)

CORS(app)

API_URL = 'http://127.0.0.1:5001'

@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def notas():
    if request.method == 'GET':
        resposta = requests.get(API_URL)
        return jsonify(resposta.json())

    if request.method == 'POST':
        requisicao = request.json
        resposta_local = requests.post(API_URL, json=requisicao)
        resposta_notion = requests.post('http://127.0.0.1:5002/', json=requisicao)
        return jsonify({
            "resposta_local": resposta_local.json(),
            "resposta_notion": resposta_notion.json()
        })

    if request.method == 'PUT':
        requisicao = request.json
        resposta = requests.put(API_URL, json=requisicao)
        return jsonify(resposta.json())

    if request.method == 'DELETE':
        requisicao = request.json
        resposta = requests.delete(API_URL, json=requisicao)
        return jsonify(resposta.json())
    
    requisicao = request.get_json()
    # Envia a nota para o microsserviço do Notion
    return jsonify(resposta.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)