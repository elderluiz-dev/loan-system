def reg_book_menu(book_id):
    print(f"ID: {book_id}")
    title = input("Título: ")
    author = input("Autor: ")
    quant = input("Quantidade de exemplares: ")

    new = {
        "id": book_id,
        "title": title,
        "author": author,
        "quant": quant
    }

    return new