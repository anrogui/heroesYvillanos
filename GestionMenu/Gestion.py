from models.Persona import Persona
from models.Villano import Villano
from models.Heroe import Heroe
import logging
import random

class GestionMenu:
    personajes = []

    def validarDatos(nombre: str, apellidos: str, fecha_nacimiento: str, identificador: str):
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        if not apellidos or not apellidos.strip():
            raise ValueError("Los apellidos no pueden estar vacíos.")
        if not fecha_nacimiento or not fecha_nacimiento.strip():
            raise ValueError("La fecha de nacimiento no puede estar vacía.")
        if not identificador or not identificador.strip():
            raise ValueError("El identificador no puede estar vacío.")

    def crear_heroe(nombre: str, apellidos: str, fecha_nacimiento: str, identificador: str):
        heroe = Heroe(nombre, apellidos, fecha_nacimiento, identificador)
        GestionMenu.validarDatos(nombre, apellidos, fecha_nacimiento, identificador)
        GestionMenu.personajes.append(heroe)

    def crearVillano(nombre: str, apellidos: str, fecha_nacimiento: str, identificador: str):
        villano = Villano(nombre, apellidos, fecha_nacimiento, identificador)
        GestionMenu.validarDatos(nombre, apellidos, fecha_nacimiento, identificador)
        GestionMenu.personajes.append(villano)


    def calcularEdad(fecha_nacimiento: str) -> int:
        from datetime import datetime
        fecha_nacimiento_dt = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
        hoy = datetime.now()
        edad = hoy.year - fecha_nacimiento_dt.year - ((hoy.month, hoy.day) < (fecha_nacimiento_dt.month, fecha_nacimiento_dt.day))
        return edad

    def buscar_personaje(self, lista_personajes, tipo_personaje, atributo, operador, valor_buscado):
        resultados = []
        
        for personaje in lista_personajes:
            
            if type(personaje).__name__.lower() == tipo_personaje.lower():#comprobar tipo de personaje
                
                valor_actual = getattr(personaje, atributo.lower(), None)#esto es para que funcione con los atributos de los personajes
                
                if valor_actual is not None:
                    if operador == "igual":
                        if str(valor_actual).lower() == str(valor_buscado).lower():
                            resultados.append(personaje)
                            
                    elif operador == "mayor":
                        if float(valor_actual) > float(valor_buscado):
                            resultados.append(personaje)
                            
                    elif operador == "menor":
                        if float(valor_actual) < float(valor_buscado):
                            resultados.append(personaje)
                            
        return resultados

    def calcular_edad(self, fecha_nacimiento: str):
        edad = self.calcularEdad(fecha_nacimiento)
        return edad

    def listarHeroes(self):
        return self.buscar_personaje(self.personajes, "Heroe", "nombre", "igual", "Heroe")

    def listarVillanos(self):
        return self.buscar_personaje(self.personajes, "Villano", "nombre", "igual", "Villano")

    def compararHyV(self, personaje1: Persona, personaje2: Persona):
       #alta desviación(diferencia de 30 puntos) es 1 y similar(diferencia de 0-29 puntos) es 0
       resultado = 0
       if personaje1.devolverPuntos()-30 > personaje2.devolverPuntos() or personaje2.devolverPuntos()-30 > personaje1.devolverPuntos():
           resultado = 1
       elif personaje1.devolverPuntos()-30 < personaje2.devolverPuntos() or  personaje2.devolverPuntos()-30 < personaje1.devolverPuntos():
           resultado = 0
       return resultado  

    def emparejar_al_azar(self):
        personaje1 = random.choice(self.personajes)
        personaje2 = random.choice(self.personajes)
        resultado = self.compararHyV(personaje1, personaje2)
        return resultado

    def logEscribir(self, mensaje: str):
        logging.basicConfig(
        filename='app.log',
        filemode='a',  # 'a' para añadir al archivo
        level=logging.INFO
        logging.info('Este mensaje se guardará en app.log')

    
    def agregar_personaje(self, personaje):
        self.personajes.append(personaje)