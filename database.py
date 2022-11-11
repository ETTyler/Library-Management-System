import sqlite3
from datetime import datetime
from dateutil.relativedelta import relativedelta


def initiate_db():
    db = sqlite3.connect('Library.db')
    cursor = db.cursor()

    with db:
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS Books (BookID INTEGER PRIMARY KEY, Genre TEXT, Title TEXT, Author TEXT, Purchase_Price INTEGER, Purchase_Date TEXT)")
        books_file = open('Book_Info.txt', 'r', encoding='utf-8')
        for line in books_file:
            print(line.strip().split(';'))
            cursor.execute("INSERT INTO Books VALUES (?,?,?,?,?,?)",
                           line.strip().split(';'))
        books_file.close()

        cursor.execute("CREATE TABLE IF NOT EXISTS Reservations (ReservationID INTEGER PRIMARY KEY, BookID INTEGER, Res_Date TEXT, CO_Date TEXT, Return_Date TEXT,"
                       "Member_ID INTEGER, FOREIGN KEY(BookID) REFERENCES Books(BookID))")
        reservations_file = open(
            'Loan_Reservation_History.txt', 'r', encoding='utf-8')
        for line in reservations_file:
            cursor.execute(
                "INSERT INTO Reservations (BookID, Res_Date, CO_Date, Return_Date, Member_ID) VALUES (?,?,?,?,?)", line.strip().split(','))
        reservations_file.close()

        print("Database created successfully")

    db.commit()
    db.close()


def book_availability(book_id):
    db = sqlite3.connect('Library.db')
    cursor = db.cursor()
    current_date = datetime.now().strftime("%Y-%m-%d")

    # if current date is greater than return date and reservation date, book is available
    with db:
        cursor.execute(
            "SELECT * FROM Reservations WHERE BookID = ? AND Return_Date = ? AND Res_Date = ?", (book_id, "null", "null"))
        result = cursor.fetchall()
        if len(result) == 0:
            return True
        else:
            return False


def check_bookID(book_id):
    db = sqlite3.connect('Library.db')
    cursor = db.cursor()

    with db:
        cursor.execute(
            "SELECT * FROM Books WHERE BookID = ?", (book_id,))
        result = cursor.fetchall()
        if len(result) == 0:
            return False
        else:
            return True


def checkout_book(book_id, member_id):
    db = sqlite3.connect('Library.db')
    cursor = db.cursor()
    co_date = datetime.now().strftime("%Y-%m-%d")

    with db:
        cursor.execute("INSERT INTO Reservations (BookID, Res_Date, CO_Date, Return_Date, Member_ID) VALUES (?,?,?,?,?)",
                       (book_id, "null", co_date, "null", member_id))
    db.commit()
    db.close()


def return_book(book_id):
    db = sqlite3.connect('Library.db')
    cursor = db.cursor()
    return_date = datetime.now().strftime("%Y-%m-%d")
    with db:
        cursor.execute(
            "UPDATE Reservations SET Return_Date = ? WHERE BookID = ? AND Return_Date = ?", (return_date, book_id, "null"))
    db.commit()
    db.close()

# helper function so I can see the current state of the database


def view_table(table_name):
    db = sqlite3.connect('Library.db')
    cursor = db.cursor()

    with db:
        cursor.execute("SELECT * FROM " + table_name)
        for row in cursor:
            print(row)
    db.commit()
    db.close()


def delete_record(reservation_id):
    db = sqlite3.connect('Library.db')
    cursor = db.cursor()

    with db:
        cursor.execute(
            "DELETE FROM Reservations WHERE ReservationID = ?", (reservation_id,))
    db.commit()
    db.close()


def reserve_book(book_id, member_id):
    db = sqlite3.connect('Library.db')
    cursor = db.cursor()
    res_date = datetime.now().strftime("%Y-%m-%d")

    with db:
        cursor.execute("INSERT INTO Reservations (BookID, Res_Date, Member_ID) VALUES (?,?,?)",
                       (book_id, res_date, member_id))
    db.commit()
    db.close()
