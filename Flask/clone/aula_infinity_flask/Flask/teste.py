# linguagens = ['Inglês', 'Português', 'Espanhol', 'Japonês']

# for index, linguagem in enumerate(linguagens, start=1):
# 	print(f'{index}ª Lingua: {linguagem}')
	


dicionario = {
	'nome': 'Eric',
	'idade': 33
}
print(dicionario.keys())
print(dicionario.values())
print(dicionario.items())

dicionario['endereco'] = 'Av lá de casa'
print(dicionario)

# print(help(dict))

for key, value in dicionario.items():
    print(f'{key}: {value}')
