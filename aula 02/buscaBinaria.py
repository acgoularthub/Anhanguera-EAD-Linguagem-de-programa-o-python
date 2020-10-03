def buscaBin(lista, numero):
	primeiro = 0
	ultimo = len(lista)-1
	found = False

	while primeiro < ultimo and not found:
		meio = (primeiro + ultimo) // 2
		if lista[meio] == numero:
			found = True
		else:
			if numero < lista[meio]:
				ultimo = meio -1
			else:
				primeiro = meio + 1
	return found 



lista = [1, 2, 3, 5, 7, 8, 8, 12, 16, 93]
print(buscaBin(lista, 12))
print(buscaBin(lista, 13))