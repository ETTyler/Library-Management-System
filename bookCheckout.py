import database as db


def id_validation(member_id):
    '''Checks if the member ID is valid'''
    if len(member_id) == 4 and member_id.isdigit():
        return True
    else:
        return False


def book_checkout(book_id, member_id):
    '''Checks if the book is available and if the member ID is valid. If both are true, the book is checked out'''
    book_exists = db.book_exists(int(book_id))
    available = db.book_availability(book_id)
    valid_ID = id_validation(str(member_id))
    if not available:
        return "Book is not available"
    elif not book_exists:
        return "Book not found"
    elif not valid_ID:
        return "Invalid member ID"
    else:
        db.checkout_book(book_id, member_id)
        return True
