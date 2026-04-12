class Astronauta:
    def __init__(self, nombre, rol):
        self.nombre = nombre
        self.rol = rol

    def saludar(self):
        return f"Hola, soy {self.nombre}, mi rol es {self.rol}"


class Sensor:
    def __init__(self, tipo):
        self.tipo = tipo
        self.valor = 0

    def medir(self, valor):
        self.valor = valor
        return f"Sensor {self.tipo} mide {self.valor}"


class SistemaControl:
    def verificar_sistemas(self):
        return "Sistemas verificados"

    def autorizar_lanzamiento(self):
        return "Lanzamiento autorizado "


class Mision:
    def __init__(self, nombre, destino):
        self.nombre = nombre
        self.destino = destino
        self.estado = "pendiente"
        self.astronautas = []

    def agregar_astronauta(self, astronauta):
        self.astronautas.append(astronauta)

    def iniciar_mision(self):
        self.estado = "en curso"
        return f"Misión {self.nombre} iniciada hacia {self.destino}"

    def finalizar_mision(self):
        self.estado = "finalizada"
        return f"Misión {self.nombre} finalizada"


class Cohete:
    def __init__(self, nombre):
        self.nombre = nombre
        self.combustible = 100
        self.estado = "apagado"
        self.sensores = []
        self.sistema_control = SistemaControl()
        self.mision = None

    def agregar_sensor(self, sensor):
        self.sensores.append(sensor)

    def asignar_mision(self, mision):
        self.mision = mision

    def encender(self):
        self.estado = "encendido"
        return f"{self.nombre} encendido"

    def lanzar(self):
        if self.estado != "encendido":
            return "Error: el cohete no está encendido"
        
        if self.sistema_control.autorizar_lanzamiento():
            return f"{self.nombre} despegando hacia {self.mision.destino}"
        
    def apagar(self):
        self.estado = "apagado"
        return f"{self.nombre} apagado"
    

    # Crear objetos
cohete = Cohete("Artemis I")
mision = Mision("Exploración Lunar", "Luna")

astro1 = Astronauta("Ana", "Comandante")
astro2 = Astronauta("Luis", "Ingeniero")

sensor_temp = Sensor("Temperatura")

# Relacionar objetos
mision.agregar_astronauta(astro1)
mision.agregar_astronauta(astro2)

cohete.asignar_mision(mision)
cohete.agregar_sensor(sensor_temp)

# Simulación
print(cohete.encender())
print(cohete.sistema_control.verificar_sistemas())
print(cohete.lanzar())

print(astro1.saludar())
print(sensor_temp.medir(75))    