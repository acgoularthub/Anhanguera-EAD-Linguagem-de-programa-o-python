class Conta:
	def __init__(self, nome, numero):
		self.cliente = nome
		self.num = numero
		self.saldo = 0.0

	def Saldo(self):
		return self.saldo

	def getCliente(self):
		return self.cliente

	def Depositar(self, valor):
		self.saldo += valor


conta1 = Conta('Anderson', 1)
conta1.Depositar(100.0)

print(conta1.getCliente())
print(conta1.Saldo())

conta1 = Conta('Jeba', 2)
conta1.Depositar(69.69)

print(conta1.getCliente())
print(conta1.Saldo())