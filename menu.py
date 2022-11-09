import tkinter as tk
import tkinter.font as tkFont
import bookSearch as bs


class App:
    def __init__(self, root):
        # setting title
        root.title("Library Management System")
        # setting window size
        width = 550
        height = 470
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        label_font = tkFont.Font(size=10)
        heading_font = tkFont.Font(size=18)

        search_label = tk.Label(root)
        search_label["font"] = label_font
        search_label["fg"] = "#333333"
        search_label["justify"] = "center"
        search_label["text"] = "Search for a book:"
        search_label.place(x=330, y=70, width=109, height=30)

        self.search_entry = tk.Entry(root)
        self.search_entry["borderwidth"] = "1px"
        self.search_entry["font"] = label_font
        self.search_entry["fg"] = "#333333"
        self.search_entry["justify"] = "center"
        self.search_entry["text"] = ""
        self.search_entry.place(x=330, y=100, width=116, height=30)

        self.search_results = tk.Message(root)
        self.search_results["font"] = label_font
        self.search_results["fg"] = "#333333"
        self.search_results["justify"] = "center"
        self.search_results["text"] = "example text"
        self.search_results.place(x=330, y=140, width=160, height=90)

        search_button = tk.Button(root)
        search_button["bg"] = "#f0f0f0"
        search_button["font"] = label_font
        search_button["fg"] = "#000000"
        search_button["justify"] = "center"
        search_button["text"] = "Go"
        search_button.place(x=450, y=100, width=47, height=30)
        search_button["command"] = self.search_button_command

        checkout_label = tk.Label(root)
        checkout_label["font"] = heading_font
        checkout_label["fg"] = "#333333"
        checkout_label["justify"] = "center"
        checkout_label["text"] = "Checkout Book"
        checkout_label.place(x=40, y=30, width=171, height=33)

        memberID_entry = tk.Entry(root)
        memberID_entry["borderwidth"] = "1px"
        memberID_entry["font"] = label_font
        memberID_entry["fg"] = "#333333"
        memberID_entry["justify"] = "center"
        memberID_entry["text"] = "MemberID"
        memberID_entry.place(x=30, y=110, width=90, height=30)

        member_label = tk.Label(root)
        member_label["font"] = label_font
        member_label["fg"] = "#333333"
        member_label["justify"] = "center"
        member_label["text"] = "Member ID:"
        member_label.place(x=40, y=80, width=70, height=25)

        book_label = tk.Label(root)
        book_label["font"] = label_font
        book_label["fg"] = "#333333"
        book_label["justify"] = "center"
        book_label["text"] = "Book ID"
        book_label.place(x=150, y=80, width=70, height=25)

        book_entry = tk.Entry(root)
        book_entry["borderwidth"] = "1px"
        book_entry["font"] = label_font
        book_entry["fg"] = "#333333"
        book_entry["justify"] = "center"
        book_entry["text"] = "Book ID"
        book_entry.place(x=140, y=110, width=90, height=30)

        checkout_button = tk.Button(root)
        checkout_button["bg"] = "#f0f0f0"
        checkout_button["font"] = label_font
        checkout_button["fg"] = "#000000"
        checkout_button["justify"] = "center"
        checkout_button["text"] = "Checkout"
        checkout_button.place(x=80, y=170, width=91, height=33)
        checkout_button["command"] = self.GButton_819_command

        returnH_label = tk.Label(root)
        returnH_label["font"] = heading_font
        returnH_label["fg"] = "#333333"
        returnH_label["justify"] = "center"
        returnH_label["text"] = "Return Book"
        returnH_label.place(x=40, y=240, width=172, height=48)

        return_label = tk.Entry(root)
        return_label["borderwidth"] = "1px"
        return_label["font"] = label_font
        return_label["fg"] = "#333333"
        return_label["justify"] = "center"
        return_label["text"] = "Book ID"
        return_label.place(x=80, y=320, width=90, height=30)

        bookID_label = tk.Label(root)
        bookID_label["font"] = label_font
        bookID_label["fg"] = "#333333"
        bookID_label["justify"] = "center"
        bookID_label["text"] = "Book ID"
        bookID_label.place(x=90, y=290, width=72, height=30)

        return_button = tk.Button(root)
        return_button["bg"] = "#f0f0f0"
        return_button["font"] = label_font
        return_button["fg"] = "#000000"
        return_button["justify"] = "center"
        return_button["text"] = "Return"
        return_button.place(x=80, y=370, width=91, height=33)
        return_button["command"] = self.GButton_154_command

        searchHeading = tk.Label(root)
        searchHeading["font"] = heading_font
        searchHeading["fg"] = "#333333"
        searchHeading["justify"] = "center"
        searchHeading["text"] = "Search "
        searchHeading.place(x=330, y=30, width=163, height=30)

        recom_label = tk.Label(root)
        recom_label["font"] = heading_font
        recom_label["fg"] = "#333333"
        recom_label["justify"] = "center"
        recom_label["text"] = "Recommendations"
        recom_label.place(x=320, y=240, width=178, height=43)

        recommendations = tk.Message(root)
        recommendations["font"] = label_font
        recommendations["fg"] = "#333333"
        recommendations["justify"] = "center"
        recommendations["text"] = "recommendations"
        recommendations.place(x=330, y=280, width=161, height=129)

    def search_button_command(self):
        book = self.search_entry.get().strip().lower()
        book_info = bs.search_book(book)
        if book_info is None:
            self.search_results["text"] = "Book not found"
        else:
            self.search_results["text"] = "Book ID: " + str(book_info[0]) + "\nTitle: " + \
                book_info[2] + "\nGenre: " + \
                book_info[1] + "\nAuthor: " + book_info[3]

    def GButton_819_command(self):
        print("command")

    def GButton_154_command(self):
        print("command")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
