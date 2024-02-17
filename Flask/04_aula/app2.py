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

@app.post('/tarefas')
# @app.input(TarefaIn) # .input(Schema) é a função que indicará qual é o schema a ser enviado
# @app.input(TarefaIn, location='form') # .input(Schema) é a função que indicará qual é o schema a ser enviado
# def create_task(json_data: dict): # json_data é o parametro onde receberemos os dados 
    # return json_data
@app.input(TarefaIn, location='json', arg_name='tarefa') # .input(Schema) é a função que indicará qual é o schema a ser enviado
def create_task(tarefa: dict): # json_data é o parametro onde receberemos os dados 
    return tarefa

if __name__ == '__main__':
    app.run(debug=True)