from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def somar():
    data: dict = request.form
    height = float(data.get('height')) # "name" do Input no HTML
    weight = float(data.get('weight')) # "name" do Input no HTML
    print(height)
    print(weight)

    imc = ( weight / ( height ** 2 ))
    categoria = ''

    if imc < 18.5:
        categoria = 'Abaixo do peso'
    elif imc < 25:
        categoria = 'Peso normal'
    elif imc < 30:
        categoria = 'Sobre Peso'
    elif imc < 35:
        categoria = 'Obesidade Grau 1'
    elif imc < 40:
        categoria = 'Obesidade Grau 2'
    else:
        categoria = 'Obesidade Grau 3'
    
    imc = str(round(imc, 2))
    
    dicionario_valores = {
        'imc': imc,
        'categoria': categoria
    }
    

    # Passando a variavel "soma" para ser renderizada pelo Jinja
    return render_template('index.html', **dicionario_valores)

if __name__ == '__main__':
    app.run(debug=True)