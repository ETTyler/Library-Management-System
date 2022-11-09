import sqlite3

db = sqlite3.connect('Library.db')
cursor = db.cursor()

# function to search for a book in the database


def search_book(book_title):
    res = cursor.execute(
        "SELECT * FROM Books WHERE LOWER(Title) = ?", (book_title,))
    for row in res:
        return row
