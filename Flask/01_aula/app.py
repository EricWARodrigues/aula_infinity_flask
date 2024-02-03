from flask import Flask, redirect, render_template, request


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
		# Precisamos da função redirect para navegar para o endpoint "/home"
    return redirect('/home') 

@app.route('/home', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/sobre-mim')
def about():
    return render_template('sobre-mim.html')

@app.route('/experiencia')
def experience():
    return render_template('experiencia.html')

@app.route('/contato', methods=['GET'])
def contact():
    return render_template('contato.html')

@app.route('/contato', methods=['POST'])
def contact_message():
    print(dict(request.form))
    remetente = request.form.get('remetente')
    assunto = request.form.get('assunto')
    mensagem = request.form.get('mensagem')
    print(remetente, assunto, mensagem)
    resposta = f'Obrigado {remetente} por enviar uma mensagem para Eric Rodrigues com o assunto {assunto}'
    return render_template('contato.html', mensagem=resposta)

if __name__ == '__main__':
    app.run(debug=True)