from apiflask import Schema
from apiflask.validators import Length
from apiflask.fields import String, Boolean


class TarefaIn(Schema):
    nome: str = String(required=True, validate=[Length(min=1)])
    completo: bool = Boolean(load_default=False)
    categoria: str = String(required=False)