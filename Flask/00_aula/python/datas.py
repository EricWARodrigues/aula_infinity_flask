# Revisão Python
# 01. Faça uma classe "Pessoa" que deve conter os seguintes atributos: nome, data_nascimento (deve ser do tipo date), peso, altura
# 02. Faça um método chamado "calcular_idade()" que irá retornar a idade da pessoa que está chamando,
# 03. Faça um método chamado "calcular_imc()" que irá retornar o IMC da pessoa.
# 04. Realize um programa que irá cadastrar 3 pessoas, armazena-las em uma lista.
from datetime import date, datetime

class Pessoa:
    def __init__(self, name: str, date: str, weight: float, height: float) -> None:
        self.nome = name
        self.nascimento = datetime.strptime(date, '%d/%m/%Y')
        self.peso = weight
        self.altura = height

    def calc_idade(self):
        data_atual = datetime.now()
        diferenca = data_atual - self.nascimento
        idade = diferenca.days // 365
        return idade
    
    def calc_imc(self):
        imc = self.peso / (self.altura ** 2)
        return imc

pessoa = Pessoa('João', '15/01/1990', 70.5, 1.75)
idade = pessoa.calc_idade()
imc = pessoa.calc_imc()
print(f'A idade é: {idade} anos')
