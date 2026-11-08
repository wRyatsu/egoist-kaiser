class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
    def depossitar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Deposito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de deposito deve ser positivo.")
    def sacar(self, valor):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                print(f"Saque de R${valor:.2f} realizado com sucesso.")
            else:
                print("Saldo insuficiente.")
        else:
            print("Valor de saque deve ser positivo.")
    def exibir_saldo(self):
        print(f"Saldo atual de {self.titular}: R${self.saldo:.2f}")

        conta1 = ContaBancaria("Joao", 1000)
        conta1.exibir_saldo()
        conta1.depossitar(500)
        conta1.exibir_saldo()
        conta1.sacar(200)
        conta1.exibir_saldo()
        conta1.sacar(1500)
        conta1.exibir_saldo()
        conta1.depossitar(-100)
        conta1.sacar(-50)
        conta1.exibir_saldo()

print("Fim do programa.")