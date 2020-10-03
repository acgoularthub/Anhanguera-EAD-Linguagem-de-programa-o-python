def valorLista():
	for i in range (1,5):
		lista.append(int(input(f'Digite sua nota {i}: ')))

def media():
	soma=0
	for i in range (len(lista)):
		soma = soma + lista[i]
	media = soma / 4
	return media


lista=[]
valorLista()
m=media()
print(m)