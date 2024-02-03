# app.py
from db import books
from http import HTTPStatus
from flask import Flask, request


app = Flask(__name__)
app.json.sort_keys = False


@app.route('/book', methods=['GET'])
def get_all_books():
    return books

@app.route('/book', methods=['POST'])
def create_book():
    data: dict = request.get_json() # Capturando o JSON enviado no Body da Requisição
    
    if data.get('nome') is None:
        return (
            {'message': 'O campo nome é obrigatório.'}, 
            HTTPStatus.BAD_REQUEST
        )
    
    if data.get('autor') is None:
        return (
            {'message': 'O campo autor é obrigatório.'}, 
            HTTPStatus.BAD_REQUEST
        )
    
    books.append({'nome': data.get('nome'), 'autor': data.get('autor')})
    return {'message': 'Livro criado com sucesso.'}


if __name__ == '__main__':
    app.run(debug=True)