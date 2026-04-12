class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo   # atributo privado

    def mostrar_saldo(self):
        return self.__saldo

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print("Depósito realizado")
        else:
            print("Monto inválido")


cuenta = CuentaBancaria(1000)

print(cuenta.mostrar_saldo())   

cuenta.depositar(500)

print(cuenta.mostrar_saldo())   