from menu import iniciar_menu 

def main():
    print("Iniciando el Gestor de Héroes y Villanos del Virgen...")
    
    try:
        iniciar_menu()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()