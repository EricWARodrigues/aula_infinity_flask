from flask import Flask 

# Criando nossa aplicação Flask
app = Flask(__name__) 

# Aqui estamos criando uma rota
@app.route('/') 
def hello_world():
    return 'Hello World'

# Retornando um Texto
@app.route('/text')
def endpoint_text():
	return 'Retornando um Texto Plano'

# Retornando um JSON
@app.route('/json')
def endpoint_api():
	return {'message': 'Aqui temos um JSON'}

# Retornando pessoas
pessoas = [
    {
        "id": 1,
        "nome": "Eric",
        "idade": 33,
        "altura": 1.75,
        "habilidades": [
              "Python",
              "Flask",
              "HTML",
              "CSS"
        ]
    },
    {
        "id": 2,
        "nome": "Alexandre",
        "idade": 54,
        "altura": 1.85,
        "habilidades": [
              "Matemática",
              "Cozinhar",
              "Computadores"
        ]
    },
    {
        "id": 3,
        "nome": "Rita",
        "idade": 52,
        "altura": 1.65,
        "habilidades": [
              "Psicologa",
              "Cozinhar",
              "Conversar"
        ]
    }
]

@app.route(f'/pessoas', methods=['GET'])
def listar_pessoas():
    return pessoas

@app.route(f'/pessoas/<int:id>', methods=['GET'])
def detalhar_pessoa(id: int):
    return pessoas[id]

# @app.route(f'/pessoa/<int:id>', methods=['GET'])
# def detalhar_pessoa3(id: int):
#     for num in range(len(pessoas)):
#          if pessoas[num]['id'] == id + 1:
#             return pessoas[num]

@app.route(f'/pessoa/<int:id>', methods=['GET'])
def detalhar_pessoa2(id: int):
    for pessoa in pessoas:
         if pessoa.get('id') == id:
              return pessoa
    return ({"message": "Pessoa não encontrada"})

# Aqui estamos executando a aplicação
if __name__ == '__main__':
    app.run(debug=True)