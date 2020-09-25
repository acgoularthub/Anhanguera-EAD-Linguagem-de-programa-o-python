salario = int (input ('entre com a informação do salário: '))
imposto = input("imposto: ")
if not imposto:
	imposto = 27.5

else:
	imposto = float(imposto)

sal = salario - (salario * (imposto * 0.01))

print ("o valor do salário menos o importo é: R$", sal)