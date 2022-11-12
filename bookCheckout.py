import database as db


def id_validation(member_id):
    if len(member_id) == 4 and member_id.isdigit():
        return True
    else:
        return False


def book_checkout(book_id, member_id):
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
        db.view_table("Reservations")
        return True
