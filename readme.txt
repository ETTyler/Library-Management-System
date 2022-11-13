Data Generation
- In the file dataGenerator.py I wrote a few functions to generate example books and reservations.
- The data for the books was produced using Googles book API through random ISBN numbers .
- This did create some issues if you look through the list of generated data as the API had no genre data and for some books no author data.
- Also the books aren't the most well known and some titles are not in English.
- The reservations were generated using random dates and random users.
- Therefore the reservations are not the most realistic as to do this I would have to check on every reservation if the book was available at that time which I didn't think was really necessary.

Recommendations Feature
- For the recommendations of books to purchase I decided to diplay the most popular books and genres on Matplotlib charts.
- As this way the data is visualised for the user rather than just getting a list of books.

Use of Classes (or lack of)
- Within this project it would have beeen possible to create classes for the books and reservations.
- However, I decided against this approach and instead separated database interactions with individual main functions to perform the tasks.
- I could have for example created a book object with attributes such as title, author, genre etc. and methods such as checkout(), return(), but I came to the conclusion that this would just overcomplicate the codebase and would provide further complexity for no real benefit. I personally feel that the code is easier to understand and maintain without the use of classes.
- The functions are extremely simple and reuse database interactions so I feel that the code is still very modular and easy to understand.
- My approach also enabled me to perform tasks with just book IDs and member IDs instead of having instantiate a book object and then call a method on it everytime I wanted to interact with the database.
- Overall while my approach may not be perfect I believe the simplicity and effectiveness of the code outweighs the benefits of using classes.