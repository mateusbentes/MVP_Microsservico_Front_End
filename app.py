from flask import Flask, request, Response, jsonify, redirect
from flask_cors import CORS
import requests

app = Flask(__name__)

CORS(app)

API_URL = 'http://127.0.0.1:5001'

@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def notas():
    if request.method == 'GET':
        response = requests.get(API_URL)
        return jsonify(response.json())

    if request.method == 'POST':
        requisicao = request.json
        response_local = requests.post(API_URL, json=requisicao)
        response_notion = requests.post('http://127.0.0.1:5002/', json=requisicao)
        return jsonify({
            "local_response": response_local.json(),
            "notion_response": response_notion.json()
        })

    if request.method == 'PUT':
        requisicao = request.json
        response = requests.put(API_URL, json=requisicao)
        return jsonify(response.json())

    if request.method == 'DELETE':
        requisicao = request.json
        response = requests.delete(API_URL, json=requisicao)
        return jsonify(response.json())
    
    requisicao = request.get_json()
    # Envia a nota para o microsserviço do Notion
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)