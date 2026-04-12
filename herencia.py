class Vehiculo:
    def __init__(self, marca, modelo, nombre):
        self.marca = marca
        self.modelo = modelo
        self.nombre = nombre

    def encender(self):
        return f"{self.nombre} encendido 🚗"

    def info(self):
        return f"{self.nombre} - {self.marca} {self.modelo}"


# 🚗 Clase Auto (para estacionamiento)
class Auto(Vehiculo):
    def __init__(self, marca, modelo, nombre, tipo):
        super().__init__(marca, modelo, nombre)
        self.tipo = tipo  # sedan, camioneta, etc.

    def estacionar(self):
        return f"{self.nombre} estacionado correctamente 🅿️"


# 🚀 Clase Cohete (inspirado en Artemis II)
class Cohete(Vehiculo):
    def __init__(self, marca, modelo, nombre, mision):
        super().__init__(marca, modelo, nombre)
        self.mision = mision

    def lanzar(self):
        return f"{self.nombre} despegando en la misión {self.mision}"

    def estacionar(self):
        return f"{self.nombre} acoplado en la estación espacial"
    
auto1 = Auto("Toyota", "Corolla", "Auto 1", "Sedan")
cohete1 = Cohete("NASA", "Orion", "Artemis II", "Luna")

print(auto1.encender())
print(auto1.estacionar())

print(cohete1.encender())
print(cohete1.lanzar())
print(cohete1.estacionar())