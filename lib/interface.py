def clear_terminal():
    print('\033[H\033[2J', end='')

def main_menu():
    print("--- SISTEMA BIBLIOTECA ---")
    print("1. Cadastrar livro")
    print("2. Listar livros")
    print("3. Pesquisar livros")
    print("4. Registrar empréstimo")
    print("5. Listar empréstimos")
    print("6. Histórico de movimentações")
    print("7. Registrar devolução")
    print("0. Sair")
    choose = input("> ")

    return choose

def search_submenu():
    print("1. Pesquisar por nome")
    print("2. Pesquisar por autor")
    print("0. Voltar")
    choose = input("> ")

    return choose