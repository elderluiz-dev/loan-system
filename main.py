from lib.register import *
from lib.search import *
from lib.interface import *

def main():
    clear_terminal()
    while True:
        opt = main_menu()

        match opt:
            case "1":
                None

            case "0":
                clear_terminal()
                print("Programa encerrado pelo usuário.")
                break

            case _:
                clear_terminal()
                print("Opção inválida")
        

if __name__ == "__main__":
    main()