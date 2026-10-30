def list_lib(lib):
    if lib == []:
        print("Nenhum livro cadastrado.\n")
    else:
        for book in lib:
            print(f"ID: {book['id']}")
            print(f"Título: {book['title']}")
            print(f"Autor: {book['author']}")
            print(f"Quantidade de exemplares: {book['quant']}\n")

def search_by_title(lib):
    title = input("Título do livro: ")
    has = False
    for book in lib:
        if title.lower() in book['title'].lower():
            print(f"ID: {book['id']}")
            print(f"Título: {book['title']}")
            print(f"Autor: {book['author']}")
            print(f"Quantidade de exemplares: {book['quant']}\n")
            has = True
    
    return has

def search_by_author(lib):
    author = input("Nome do autor: ")
    has = False
    for book in lib:
        if author.lower() in book['author'].lower():
            print(f"ID: {book['id']}")
            print(f"Título: {book['title']}")
            print(f"Autor: {book['author']}")
            print(f"Quantidade de exemplares: {book['quant']}\n")
            has = True
    
    return has