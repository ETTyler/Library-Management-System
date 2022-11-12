import database as db


def select_books(num_books):
    book_list = db.popular_books()
    return book_list[:num_books]


print(select_books(3))
