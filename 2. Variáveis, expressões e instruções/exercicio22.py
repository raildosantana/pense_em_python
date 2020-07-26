#O volume de uma esfera com raio r é 4/3 * pi * r^3 – Volume de uma esfera.. 
# Qual é o volume de uma esfera com raio 5?
volume = (4/3) * 3.14 * pow(5,3)
print("Volume de uma esfera de raio 5: %.2f"%(volume))

#Suponha que o preço de capa de um livro seja R$ 24,95, mas as livrarias recebem um desconto de 40%. 
#O transporte custa R$ 3,00 para o primeiro exemplar e 75 centavos para cada exemplar adicional. 
#Qual é o custo total de atacado para 60 cópias?
def custo(totalLivros):
	transporte = 0
	if totalLivros >= 1:
		transporte += 3
		transporte += (totalLivros - 1) * 0.75
	precoLivro = 24.95 * 0.6
	totalPrecoLivro = totalLivros *precoLivro
	custoTotal = transporte + totalPrecoLivro
	return custoTotal

print("Preço dos livros: %.2f"%custo(60))

# Se eu sair da minha casa às 6:52 e correr 1 quilômetro a um certo passo (8min15s por quilômetro), 
# então 3 quilômetros a um passo mais rápido (7min12s por quilômetro) e 1 quilômetro no mesmo passo 
# usado em primeiro lugar, que horas chego em casa para o café da manhã?
def tempo(minutos,segundos):
	return minutos * 60 + segundos

def tempoTotal(quilometro,tempo):
	return quilometro * tempo

minutos = (tempoTotal(2,tempo(8,15)) + tempoTotal(3,tempo(7,12)))//60
horas = 6 + ((52 + minutos) // 60)
minutos = minutos - 8
print("Tempo: %d:%d"%(horas,minutos))
