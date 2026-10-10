from GestionMenu.Gestion import GestionMenu
from models.Villano import Villano
from models.Heroe import Heroe

def iniciar_menu():
    gestor = GestionMenu()
    opcion=""
    while opcion != "6":
        print(" HÉROES Y VILLANOS")
        print("1. Crear Villano")
        print("2. Crear Héroe")
        print("3. Buscar personaje")
        print("4. Mostrar edad de un personaje")
        print("5. Emparejar Héroe vs Villano al azar")
        print("6. Salir")
        
        opcion = input("\nElige una opción: ")
        
        if opcion == "1":
            print("\nCreando villano")
            nombre = input("Nombre: ")
            apellidos = input("Apellidos: ")
            fecha = input("Fecha de nacimiento (DD/MM/YYYY): ")
            identificador = input("Identificador: ")
            
            nuevo_villano = Villano(nombre, apellidos, fecha, identificador)
            gestor.agregar_personaje(nuevo_villano)
            print(f"Villano {nombre} creado")
            
        elif opcion == "2":
            print("\nCreando héroe")
            nombre = input("Nombre: ")
            apellidos = input("Apellidos: ")
            fecha = input("Fecha de nacimiento (DD/MM/YYYY): ")
            identificador = input("Identificador: ")
            
            nuevo_heroe = Heroe(nombre, apellidos, fecha, identificador)
            gestor.agregar_personaje(nuevo_heroe)
            print(f"Héroe {nombre} creado")
            
        elif opcion == "3":
            print("\nBuscador por filtros")
            tipo = input("¿Qué buscas? (Heroe / Villano): ")
            atributo = input("¿Por qué atributo? (ej. nombre, GITGod, chagepeteador): ")
            operador = input("Operador (igual / mayor / menor): ")
            valor = input("Valor buscado (ej. Fernando, 50): ")
            

            resultados = gestor.buscar_personaje(gestor.personajes, tipo, atributo, operador, valor)
            
            if resultados:
                print(f"\nse encontraron {len(resultados)} RESULTADOS ---")
                for p in resultados:
                    # Usamos getattr para mostrar el valor por pantalla
                    valor_mostrado = getattr(p, atributo.lower(), 'none')#devuelve el valor si existe,si no devuelve none
                    print(f"- {p.nombre} {p.apellidos} (Puntuación: {p.puntuacion_total})  {atributo}: {valor_mostrado}")
            else:
                print("\nNingún personaje encontrado")

        elif opcion == "4":
            print("\n dime el identificador del personaje para calcular su edad")
            identificador = input("Identificador: ")
            personaje = gestor.buscar_personaje(gestor.personajes, "Personaje", "identificador", "igual", identificador)
            if personaje:
                print(f"La edad del personaje es {gestor.calcular_edad(personaje[0].fecha_nacimiento)}")
        elif opcion == "5":
            print("\nEmparejamiento al azar")
            resultado = gestor.emparejar_al_azar()
            if resultado == 1:
                print("\nAlta desviación")
            elif resultado == 0:
                print("\nHéroe pierde al azar")
            
        elif opcion == "6":
            print("Saliendo")
        else:
            print("\nOpción no válida. Por favor, introduce un número del 1 al 6.")