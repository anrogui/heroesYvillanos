class Persona:
    def __init__(self, nombre, apellidos, fecha_nacimiento, identificador):
        self.nombre = nombre
        self.apellidos = apellidos  
        self.fecha_nacimiento = fecha_nacimiento
        self.identificador = identificador
        self.puntos_totales = 0

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, Apellidos: {self.apellidos}, Fecha: {self.fecha_nacimiento}, ID: {self.identificador}, Puntos: {self.puntos_totales}"

    def devolverPuntos(self):
        return self.puntos_totales