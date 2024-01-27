from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index2.html')

@app.route('/', methods=['POST'])
def somar():
    data = dict(request.form)
    numero1 = data.get('num-1') # "name" do Input no HTML
    numero2 = data.get('num-2') # "name" do Input no HTML 
    
    # Convertendo para Float
    if numero1.strip() != '':
        numero1 = float(numero1)
    else:
        numero1 = 0

    # Convertendo para Float
    if numero2.strip() != '':
        numero2 = float(numero2)
    else:
        numero2 = 0
    
    resultado = numero1 + numero2

    dicionario_valores = {
        'soma': resultado
    }

    # Passando a variavel "soma" para ser renderizada pelo Jinja
    return render_template('index2.html', **dicionario_valores)

if __name__ == '__main__':
    app.run(debug=True)