import database as db


def return_book(book_id):
    available = db.book_availability(book_id)
    valid_ID = db.check_bookID(book_id)
    if available:
        return 'Book is already available'
    elif not valid_ID:
        return 'Invalid ID'
    else:
        db.return_book(book_id)
        return True
