
class Profesor:

    def __init__(self, name: str, asignatura: str, age: int):
        self.name = name
        self.asignatura = asignatura

    def saludar(self):
        return f"Hola, soy {self.name} Profe de {self.asignatura}"
    
ProfeUno = Profesor( "Pepe", "Programación ", 25)

print(ProfeUno.saludar())


