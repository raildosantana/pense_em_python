def funcao(teste):
	print(teste)

def do_four(funcao,valor):
	for i in range(4):
		funcao(valor)

do_four(funcao,"Python")