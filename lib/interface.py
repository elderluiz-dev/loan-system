def clear_terminal():
    print('\033[H\033[2J', end='')

def main_menu():
    print("--- SISTEMA BIBLIOTECA ---")
    print("1. Cadastrar livro")
    print("2. Listar livros")
    print("3. Registrar empréstimo")
    print("4. Listar empréstimos")
    print("5. Histórico de movimentações")
    print("6. Registrar devolução")
    print("0. Sair")
    choose = input("> ")

    return choose