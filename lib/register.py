def reg_book_menu(book_id):
    print(f"ID: {book_id}")
    title = input("Título: ")
    author = input("Autor: ")
    quant = int(input("Quantidade de exemplares: "))

    new = {
        "id": book_id,
        "title": title,
        "author": author,
        "quant": quant
    }

    return new

def reg_loan(lib):
    for book in lib:
        if book['quant'] > 0:
            print(f"{book['id']}. {book['title']}")

    choose = int(input("Digite o ID do livro a ser emprestado: "))

    for book in lib:
        if choose == book['id']:
            if book['quant'] > 0:
                book['quant'] -= 1
                selection = book['id']

    reader = input("Digite o nome do leitor: ")

    new_loan = {
        "book": selection,
        "reader": reader
    }

    return new_loan

def reg_return(loans, lib):
    name = input("Digite o nome do leitor: ")
    
    for loan in loans:
        if name.lower() == loan['reader'].lower():
            reader = loan

    print('\033[H\033[2J', end='')
    print(f"Livros emprestados para: {name}")
    
    for book in lib:
        if reader['book'] == book['id']:
            print(f"{book['id']}. {book['title']}")

    choose = int(input("Digite o ID do livro que deseja devolver: "))

    for loan in loans:
        if name.lower() == loan['reader'].lower() and choose == loan['book']:
            loans.remove(loan)

            for book in lib:
                if choose == book['id']:
                    book['quant'] += 1

            return True
        
    return False