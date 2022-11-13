from random import randint, randrange
import json
from urllib.request import urlopen
import time
from datetime import datetime
from dateutil.relativedelta import relativedelta


def random_date():
    '''Generates a random date for example reservation data'''
    start = time.mktime(time.strptime('1/1/2018', '%m/%d/%Y'))
    end = time.mktime(time.strptime('1/1/2022', '%m/%d/%Y'))
    t = start + randrange(end - start)
    return time.strftime('%Y-%m-%d', time.localtime(t))


def generate_book_data():
    '''Generates a list of book data using the Google Books API and randomly generated data'''
    # the google books API doesn't inlcude genre data, so I randomly selected them for the example books
    genres = ['Fantasy', 'Sci-Fi', 'Romance', 'Mystery', 'Horror',
              'Thriller', 'Drama', 'Comedy', 'Action', 'Adventure']
    book_data = []
    count = 1
    while True:
        api = "https://www.googleapis.com/books/v1/volumes?q=isbn:"
        isbn = str(randint(1000000000, 9999999999))
        response = urlopen(api + str(isbn))
        data = json.load(response)
        # the api has a limit of 1 request per second, so I added a sleep to avoid hitting the limit
        time.sleep(1.2)
        if data['totalItems'] > 0:
            bookTitle = data['items'][0]['volumeInfo']['title']
            # some books don't have an author listed so are labeled as "Unknown"
            try:
                bookAuthor = data['items'][0]['volumeInfo']['authors'][0]
            except:
                bookAuthor = 'Unknown'
            book_data.append([count, genres[randint(0, 9)], bookTitle,
                             bookAuthor, randint(1, 20), random_date()])
            if count == 50:
                break
            count += 1

    return book_data


def print_book_data():
    '''Prints the book data to the console so it can be copied into the text file'''
    book_data = generate_book_data()
    for i in book_data:
        print(';'.join(map(str, i)))


def generate_reservation_data():
    '''Generates a list of reservations using randomly generated data'''
    reservation_data = []
    for i in range(0, 200):
        date = random_date()
        return_date = (datetime.strptime(date, '%Y-%m-%d') +
                       relativedelta(months=+1)).strftime('%Y-%m-%d')
        reservation_data.append(
            [randint(1, 50), "null", date, return_date, randint(1000, 9999)])

    return reservation_data


def print_reservation_data():
    '''Prints the reservation data to the console so it can be copied into the text file'''
    reservation_data = generate_reservation_data()
    for i in reservation_data:
        print(','.join(map(str, i)))
