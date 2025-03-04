from game import Game

def choose_mode():
    while True:
        print("Selecciona el modo de juego:")
        print("1. Modo Normal (dados aleatorios)")
        print("2. Modo Desarrollador (elegir valores de los dados)")
        choice = input("Ingresa el número correspondiente al modo que deseas: ")

        if choice == "1":
            return False  # Modo normal
        elif choice == "2":
            return True   # Modo desarrollador
        else:
            print("Opción inválida. Por favor, ingresa 1 o 2.")

if __name__ == "__main__":
    developer_mode = choose_mode()  # Pregunta al usuario qué modo desea
    game = Game(developer_mode=developer_mode)  # Inicia el juego en el modo seleccionado
    game.start_game()



