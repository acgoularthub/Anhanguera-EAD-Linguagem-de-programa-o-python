def calculaImposto(salario, imposto):
	result = salario - (salario * (imposto * 0.01))
	return result

imposto = float (input("digite seu imposto: "))
salario = float (input("digite seu salário: "))

print("Seu salário com o imposto descontado é: R$", calculaImposto(salario, imposto))