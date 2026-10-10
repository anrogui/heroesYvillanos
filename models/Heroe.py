from models.Persona import Persona
import random

class Heroe(Persona):
    def __init__(self, nombre, apellidos, fecha_nacimiento, identificador):
        
        super().__init__(nombre, apellidos, fecha_nacimiento, identificador)
        self.codigoLimpio = random.randint(1,100)
        self.bienDocumentado = random.randint(1,100)
        self.GITGod = random.randint(1,100)
        self.Arquitecto = random.randint(1,100)
        self.detallista = random.randint(1,100)

    def __str__(self) -> str:
        return f"{super().__str__()}, Codigo Limpio: {self.codigoLimpio}, Documentado: {self.bienDocumentado}, GIT God: {self.GITGod}, Arquitecto: {self.Arquitecto}, Detallista: {self.detallista}"


    def devolverPuntos(self):
        suma_puntos = self.codigoLimpio + self.bienDocumentado + self.GITGod + self.Arquitecto + self.detallista
        return self.puntos_totales + (suma_puntos / 5)