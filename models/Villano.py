from models.Persona import Persona
from random import random


class Villano(Persona):
    def __init__(self, nombre, Apellidos, fecha_nacimiento, identificador, puntos_totales, Chatgepeteador,EntregadorTardío,Ausencias,Hablador):
        super().__init__(nombre, Apellidos, fecha_nacimiento, identificador, puntos_totales)
        self.Chatgepeteador=random.randint(1,100)
        self.EntregadorTardío=random.randint(1,100)
        self.Ausencias=random.randint(1,100)
        self.Hablador=random.randint(1,100)

    def __str__(self) -> str:
        return f"{super().__str__()}, Chatgepeteador: {self.Chatgepeteador}, Entregador Tardío: {self.EntregadorTardío}, Ausencias: {self.Ausencias}, Hablador: {self.Hablador}"

    def devolverPuntos(self):
        return np.mean(self.puntos_totales + self.Chatgepeteador + self.EntregadorTardío + self.Ausencias + self.Hablador)