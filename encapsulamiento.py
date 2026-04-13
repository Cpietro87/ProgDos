# Ejemplo de encapsulamiento en Python
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

# Intento de acceso directo al atributo privado (no recomendado)
class Alumno:
    def __init__(self, nota):
        self.__nota = nota

    @property
    def nota(self):
        return self.__nota

    @nota.setter
    def nota(self, valor):
        if 0 <= valor <= 10:
            self.__nota = valor
        else:
            print("Nota inválida")

alumno = Alumno(8)
print(alumno.nota)  
alumno.nota = 9
print(alumno.nota)
alumno.nota = 11 
