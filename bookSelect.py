import database as db


def select_books(num_books):
    '''Takes a number of books and returns a list of the most loaned books'''
    book_list = db.popular_books()
    return book_list[:num_books]


def select_genres():
    '''Returns a list of each genres popularity in order'''
    genre_list = db.popular_genres()
    return genre_list
