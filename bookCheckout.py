import database as db


def id_validation(member_id):
    '''Checks if the member ID is valid'''
    if len(member_id) == 4 and member_id.isdigit():
        return True
    else:
        return False


def book_checkout(book_id, member_id):
    '''Checks if the book is available and if the member ID is valid. If both are true, the book is checked out. Assumes the input is a string.'''
    if not book_id.isdigit():
        return 'Invalid book ID'
    book_exists = db.book_exists(int(book_id))
    available = db.book_availability(book_id)
    valid_ID = id_validation(str(member_id))
    if not valid_ID:
        return "Invalid member ID"
    elif not book_exists:
        return "Book not found"
    elif not available:
        return "Book is not available"
    else:
        db.checkout_book(book_id, member_id)
        return True


if __name__ == '__main__':
    # Testing
    print(book_checkout('1', '1234'))
    print(book_checkout('e', '12343'))
    print(book_checkout('2', 'eddfd'))
    print(id_validation('1234'))
    print(id_validation('dfddfdsf'))
    print(id_validation('1234333'))
