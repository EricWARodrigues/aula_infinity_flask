from db import pessoas
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/pessoa/<int:id>')
def detalhar_pessoa(id: int):
	pessoa = pessoas[id]
	return render_template('index.html', nome=pessoa.get('nome'), idade=pessoa.get('idade'))

if __name__ == '__main__':
    app.run(debug=True)