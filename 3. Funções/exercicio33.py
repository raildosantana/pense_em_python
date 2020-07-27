
def grid(linhas = 1,colunas = 1,vertical = 6, horizontal = 6):
	for i in range(linhas * horizontal + 1):
		if i == 0 or not ((i) % horizontal):
			print("+ ",end ="")
			for j in range(0, (colunas * vertical) - 1):
				if not ((j+1) % vertical):
					print("+ ",end = "")
				else:
					print("- ",end = "")
			print("+")
		else:
			print("| ",end ="")
			for j in range(0, (colunas * vertical) - 1):
				if not ((j+1) % vertical):
					print("| ",end = "")
				else:
					print("  ",end = "")
			print("|")


grid(3,3,2,2)