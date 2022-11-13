import sqlite3
from datetime import datetime
from dateutil.relativedelta import relativedelta


def initiate_db():
    '''Creates the database and tables if they don't exist'''
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


# Functions to modify the database

def checkout_book(book_id, member_id):
    '''Checks out a book using its ID and a member ID'''
    db = sqlite3.connect('Library.db')
    cursor = db.cursor()
    co_date = datetime.now().strftime("%Y-%m-%d")

    with db:
        cursor.execute("INSERT INTO Reservations (BookID, Res_Date, CO_Date, Return_Date, Member_ID) VALUES (?,?,?,?,?)",
                       (book_id, "null", co_date, "null", member_id))
    db.commit()
    db.close()


def reserve_book(book_id, member_id):
    '''Reserves a book using its ID and a member ID'''
    db = sqlite3.connect('Library.db')
    cursor = db.cursor()
    available = book_reserved(book_id)
    if available:
        res_date = datetime.now().strftime("%Y-%m-%d")
        with db:
            cursor.execute("INSERT INTO Reservations (BookID, Res_Date, CO_Date, Return_Date, Member_ID) VALUES (?,?,?,?,?)",
                           (book_id, res_date, "null", "null", member_id))
    else:
        return False
    db.commit()
    db.close()
    return True


def return_book(book_id):
    '''Returns a book using its ID'''
    db = sqlite3.connect('Library.db')
    cursor = db.cursor()
    return_date = datetime.now().strftime("%Y-%m-%d")
    with db:
        cursor.execute(
            "UPDATE Reservations SET Return_Date = ? WHERE BookID = ? AND Return_Date = ?", (return_date, book_id, "null"))
    db.commit()
    db.close()


def delete_record(reservation_id):
    '''Deletes a record from the database using its ID'''
    db = sqlite3.connect('Library.db')
    cursor = db.cursor()

    with db:
        cursor.execute(
            "DELETE FROM Reservations WHERE ReservationID = ?", (reservation_id,))
    db.commit()
    db.close()


# 1. Validation functions

def book_exists(book_id):
    '''Checks if a book exists in the database using its ID'''
    db = sqlite3.connect('Library.db')
    cursor = db.cursor()

    with db:
        cursor.execute("SELECT * FROM Books WHERE BookID = ?", (book_id,))
        result = cursor.fetchall()
        if len(result) == 0:
            return False
        else:
            return True


def book_availability(book_id):
    '''Checks if a book is available for checkout'''
    db = sqlite3.connect('Library.db')
    cursor = db.cursor()

    with db:
        cursor.execute(
            "SELECT * FROM Reservations WHERE BookID = ? AND Return_Date = ? AND Res_Date = ?", (book_id, "null", "null"))
        result = cursor.fetchall()
        if len(result) == 0:
            return True
        else:
            return False


def book_reserved(book_id):
    '''Checks if a book is reserved using its ID'''
    db = sqlite3.connect('Library.db')
    cursor = db.cursor()

    with db:
        cursor.execute(
            "SELECT * FROM Reservations WHERE BookID = ? AND CO_Date = ? AND Return_Date = ?", (book_id, "null", "null"))
        result = cursor.fetchall()
        if len(result) == 0:
            return True
        else:
            return False


# 2. Data retrieval functions


def popular_books():
    '''Returns the most popular books in the database in order'''
    db = sqlite3.connect('Library.db')
    cursor = db.cursor()

    with db:
        cursor.execute(
            "SELECT Reservations.BookID, COUNT(Reservations.BookID), Books.Title, Books.Author, Books.Genre FROM Reservations INNER JOIN Books ON Reservations.BookID = Books.BookID GROUP BY Reservations.BookID ORDER BY COUNT(Reservations.BookID) DESC")
        return cursor.fetchall()


def popular_genres():
    '''Returns the most popular genres in the database in order'''
    db = sqlite3.connect('Library.db')
    cursor = db.cursor()

    with db:
        cursor.execute("SELECT Books.Genre, COUNT(Books.Genre) FROM Reservations INNER JOIN Books ON Reservations.BookID = Books.BookID GROUP BY Books.Genre ORDER BY COUNT(Books.Genre) DESC")
    return cursor.fetchall()


def book_info(book_id):
    '''Returns the information of a book using its ID'''
    db = sqlite3.connect('Library.db')
    cursor = db.cursor()

    with db:
        cursor.execute("SELECT * FROM Books WHERE BookID = ?", (book_id,))
        return cursor.fetchall()


def search_book(book_title):
    '''Returns the information of a book using its title'''
    db = sqlite3.connect('Library.db')
    cursor = db.cursor()
    res = cursor.execute(
        "SELECT * FROM Books WHERE LOWER(Title) = ?", (book_title,))
    return res.fetchall()


# helper function so you can see the current state of the database easily

def view_table(table_name):
    '''Prints the contents of a table'''
    db = sqlite3.connect('Library.db')
    cursor = db.cursor()

    with db:
        cursor.execute("SELECT * FROM " + table_name)
        for row in cursor:
            print(row)
    db.commit()
    db.close()
