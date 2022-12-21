from conta import Conta
from cliente import Cliente

conta1 = Conta(123, "Nico", 55.5, 1000.0)
conta2 = Conta(321, "Marcos", 100.0, 1000.0)
conta3 = Conta(321, "Marcos", 100.0, 1000.0)

cliente1 = Cliente("Marcos")

codigo_banco = Conta.codigos_bancos()

print(codigo_banco["Bradesco"])