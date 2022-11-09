import sqlite3


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


initiate_db()
