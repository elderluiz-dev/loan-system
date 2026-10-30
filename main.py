from lib.register import *
from lib.shows import *
from lib.interface import *
import json

def main():
    clear_terminal()
    try:
        with open("lib.json", "r") as file:
            lib = json.load(file)
            book_id = int(lib[-1]['id']) + 1
    except FileNotFoundError:
            lib = []
            book_id = 0

    while True:
        opt = main_menu()

        match opt:
            case "1":
                clear_terminal()
                new_book = reg_book_menu(book_id)
                lib.append(new_book)
                book_id += 1
                clear_terminal()
                print("Livro cadastrado com sucesso!\n")

            case "2":
                clear_terminal()
                list_lib(lib)

            case "3":
                clear_terminal()
                if lib != []:
                    sub = search_submenu()
                    match sub:
                        case "1":
                            clear_terminal()
                            if search_by_title(lib) == False:
                                print("Título não encontrado.\n")
                        case "2":
                            clear_terminal()
                            if search_by_author(lib) == False:
                                print("Autor não encontrado.\n")
                        case "0":
                            clear_terminal()
                        case _:
                            clear_terminal()
                            print("Opção inválida\n")
                else:
                    print("Nenhum livro cadastrado.\n")

            case "0":
                clear_terminal()
                with open("lib.json", "w", encoding="utf-8") as file:
                    json.dump(lib, file, indent=4, ensure_ascii=False)

                print("Programa encerrado pelo usuário.")
                break

            case _:
                clear_terminal()
                print("Opção inválida\n")
        

if __name__ == "__main__":
    main()