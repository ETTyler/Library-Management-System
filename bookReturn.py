import database as db


def return_book(book_id):
    '''Checks if the book is reserved and if it is, returns the book'''
    available = db.book_availability(book_id)
    valid_ID = db.book_exists(book_id)
    if not valid_ID:
        return 'Invalid book ID'
    elif available:
        return 'Book has not been checked out'
    else:
        db.return_book(book_id)
        return True


if __name__ == '__main__':
    # Testing
    print(return_book('1'))
    print(return_book('343'))
    print(return_book('sdfds'))
