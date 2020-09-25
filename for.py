def criaSequencia(): #cria função que recebe o parâmetro inicial e final do for
	i = int(input("inicio: "))
	f = int(input("fim: "))

	for i in range(i,f+1, 1):
		print(i)

criaSequencia() #chama a função criada

print("\n")

for i in range (6): #cria uma sequncia de 6 numeros a partir do 0.
	print (i)

print("\n")

for i in range (1,6): #cria uma sequencia de numeros de 1 a 5, o limitedo range é a esquerda do ultimo numero
	print(i)

print("\n")

for i in range(6,0,-1): #decrementa de 1 em 1: 6,5,4,3,2,1,0.
	print(i)

print("\n")

for i in range(6,0,-2): #decrementa de 2 em 2: 6,4,2,0.
	print(i)

print("\n")

