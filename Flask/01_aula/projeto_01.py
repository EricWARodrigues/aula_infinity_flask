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

pessoas = [
    {
        "id": 0,
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
        "id": 1,
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
        "id": 2,
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

# Retornando pessoas
id = 0
rota = f'/pessoa'
@app.route(f'/pessoa')
def listar_pessoas():
    pessoas = [
        {
            "id": 0,
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
            "id": 1,
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
            "id": 2,
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
    return pessoas

# Aqui estamos executando a aplicação
if __name__ == '__main__':
    app.run(debug=True)