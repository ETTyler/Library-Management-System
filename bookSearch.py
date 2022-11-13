import database as db


def book_search(book):
    '''Takes either a book ID or a book title and returns a list of books that match the search'''
    if (book.isdigit()):
        if (db.book_exists(book)):
            return db.book_info(book)
        else:
            return False
    else:
        return db.search_book(book)
