def buscaSeq(lista, numb):
	pos = 0
	x = False

	while pos<len(lista) and not x:
		if lista[pos] == numb:
			x = True
		else:
			pos = pos + 1
	return x


lista = [7, 8, 5, 2, 3, 9, 12, 16, 93, 1]

print(buscaSeq(lista, 12))
print(buscaSeq(lista, 13))