import database as db


def id_validation(member_id):
    if len(member_id) == 4 and member_id.isdigit():
        return True
    else:
        return False


def book_checkout(book_id, member_id):
    available = db.book_availability(book_id)
    valid_ID = id_validation(str(member_id))
    print(member_id)
    print(valid_ID)
    if not available:
        # return variable to open reservation option and then run reservation function
        return "Book is not available"
    elif not valid_ID:
        return "Invalid ID"
    else:
        db.checkout_book(book_id, member_id)
        db.view_table("Reservations")
        return True
