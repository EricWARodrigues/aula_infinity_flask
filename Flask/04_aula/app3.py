from db import tarefas
from schema import TarefaIn
from apiflask import APIFlask
from flask import render_template
from http import HTTPStatus

app = APIFlask(__name__)
app.json.sort_keys = False

# Web Routes
@app.get('/tarefas')
def index():
    return render_template('index.html', tarefas = tarefas)

# Api Routes
@app.get('/api/tarefas')
@app.doc(tags=['Tarefas'])
def listar_tarefas():
    return tarefas

@app.get('/api/tarefas/<int:id>')
@app.doc(tags=['Tarefas'])
def listar_tarefas_por_id(id):
    for tarefa in tarefas:
        if tarefa.get('id') == id:
            return ({"nome": tarefa.get('nome'), "completo": tarefa.get('completo')}, 200)
    return ({"message": "Tarefa não encontrada"}, HTTPStatus.IM_A_TEAPOT)

@app.post('/api/tarefas')
@app.input(TarefaIn, arg_name='tarefa_in')
@app.doc(tags=['Tarefas'])
def cadastrar_tarefa(tarefa_in: dict):
    maior_id = None
    for tarefa in tarefas:
        if maior_id is None or tarefa.get('id') > maior_id:
            maior_id = tarefa.get('id')

    novo_id = maior_id + 1
    tarefa_in.update({ 'id': novo_id })
    tarefas.append(tarefa_in)
    return ({'message': 'Tarefa Cadastrada com Sucesso'}, 201)

@app.put('/api/tarefas/<int:id>')
@app.input(TarefaIn, arg_name='tarefa_put')
@app.doc(tags=['Tarefas'])
def atualizar_tarefa(id: int, tarefa_put: dict):
    for i, tarefa in enumerate(tarefas):
        if tarefa.get('id') == id:
            tarefa.update(tarefa_put)
            return ({"message": "Tarefa atualizada com sucesso"}, 201)
    return ({"message": "Tarefa não encontrada"}, 400)

@app.delete('/api/tarefas/<int:id>')
@app.doc(tags=['Tarefas'])
def deletar_tarefa(id: int):
    for i, tarefa in enumerate(tarefas):
        if tarefa.get('id') == id:
            tarefas.pop(i)
            return ({"message": "Tarefa excluída com sucesso"}, 201)
    return ({"message": "Tarefa não encontrada"}, 400)

if __name__ == '__main__':
    app.run(debug=True)