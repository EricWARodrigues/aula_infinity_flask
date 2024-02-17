from db import tarefas
from flask import Flask, render_template

from apiflask import APIFlask

app = Flask(__name__)
app2 = APIFlask(__name__)
app2.json.sort_keys = False

# WEB Routes
@app.route('/tarefa', methods=['GET'])
def listar_tarefas():
    return render_template('index.html', tarefas=tarefas)

# API Routes
@app2.get('/tarefa/<int:id>')
def listar_tarefas(id: int):
    return {'id': id}

@app2.get('/api/tarefas')
def listar_tarefas2():
    return tarefas

if __name__ == '__main__':
    # app.run(debug=True)
    app2.run(debug=True)