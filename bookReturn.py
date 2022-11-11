import database as db


def return_book(book_id):
    available = db.book_availability(book_id)
    valid_ID = db.check_bookID(book_id)
    if not valid_ID:
        return 'Invalid book ID'
    elif available:
        return 'Book has not been checked out'
    else:
        db.return_book(book_id)
        return True
