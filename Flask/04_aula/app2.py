from apiflask import APIFlask, Schema
from apiflask.validators import Length
from apiflask.fields import String, Float, Boolean
from schema import TarefaIn

app = APIFlask(__name__)
# Criando o Schema
# class Tarefas(Schema):
#     nome: str = String(required=True, validate=[Length(min=3, max=255)])
#     categoria: str = String(required=False)
#     completo: bool = Boolean(required=True)

@app.get('/api/tarefas')
def get_tasks():
    return {"teste": "teste"}

@app.post('/api/tarefas')
# @app.input(TarefaIn) # .input(Schema) é a função que indicará qual é o schema a ser enviado
# @app.input(TarefaIn, location='form') # .input(Schema) é a função que indicará qual é o schema a ser enviado
# def create_task(json_data: dict): # json_data é o parametro onde receberemos os dados 
    # return json_data
@app.input(TarefaIn, location='json', arg_name='tarefa', example={"nome": "Nome tarefa", "completo": True}) # .input(Schema) é a função que indicará qual é o schema a ser enviado
def create_task(tarefa: dict): # json_data é o parametro onde receberemos os dados 
    return tarefa

if __name__ == '__main__':
    app.run(debug=True)