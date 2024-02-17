from db import tarefas
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/tarefa', methods=['GET'])
def listar_tarefas():
    return render_template('index.html', tarefas=tarefas)

if __name__ == '__main__':
    app.run(debug=True)