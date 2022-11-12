import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
import bookSearch as bs
import bookCheckout as bc
import bookReturn as br
import database as db


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
        self.search_entry.place(x=330, y=100, width=116, height=30)

        self.search_results = tk.Message(root)
        self.search_results["font"] = label_font
        self.search_results["fg"] = "#333333"
        self.search_results["justify"] = "center"
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

        self.memberID_entry = tk.Entry(root)
        self.memberID_entry["borderwidth"] = "1px"
        self.memberID_entry["font"] = label_font
        self.memberID_entry["fg"] = "#333333"
        self.memberID_entry["justify"] = "center"
        self.memberID_entry["text"] = "MemberID"
        self.memberID_entry.place(x=30, y=110, width=90, height=30)

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
        book_label["text"] = "Book ID:"
        book_label.place(x=150, y=80, width=70, height=25)

        self.book_entry = tk.Entry(root)
        self.book_entry["borderwidth"] = "1px"
        self.book_entry["font"] = label_font
        self.book_entry["fg"] = "#333333"
        self.book_entry["justify"] = "center"
        self.book_entry["text"] = "Book ID"
        self.book_entry.place(x=140, y=110, width=90, height=30)

        checkout_button = tk.Button(root)
        checkout_button["bg"] = "#f0f0f0"
        checkout_button["font"] = label_font
        checkout_button["fg"] = "#000000"
        checkout_button["justify"] = "center"
        checkout_button["text"] = "Checkout"
        checkout_button.place(x=80, y=170, width=91, height=33)
        checkout_button["command"] = self.checkout_button_command

        returnH_label = tk.Label(root)
        returnH_label["font"] = heading_font
        returnH_label["fg"] = "#333333"
        returnH_label["justify"] = "center"
        returnH_label["text"] = "Return Book"
        returnH_label.place(x=40, y=240, width=172, height=48)

        self.return_entry = tk.Entry(root)
        self.return_entry["borderwidth"] = "1px"
        self.return_entry["font"] = label_font
        self.return_entry["fg"] = "#333333"
        self.return_entry["justify"] = "center"
        self.return_entry["text"] = "Book ID:"
        self.return_entry.place(x=80, y=320, width=90, height=30)

        bookID_label = tk.Label(root)
        bookID_label["font"] = label_font
        bookID_label["fg"] = "#333333"
        bookID_label["justify"] = "center"
        bookID_label["text"] = "Book ID:"
        bookID_label.place(x=90, y=290, width=72, height=30)

        return_button = tk.Button(root)
        return_button["bg"] = "#f0f0f0"
        return_button["font"] = label_font
        return_button["fg"] = "#000000"
        return_button["justify"] = "center"
        return_button["text"] = "Return"
        return_button.place(x=80, y=370, width=91, height=33)
        return_button["command"] = self.return_button_command

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
        recom_label.place(x=320, y=240, width=200, height=45)

        recommendations = tk.Button(root)
        recommendations["bg"] = "#f0f0f0"
        recommendations["font"] = label_font
        recommendations["fg"] = "#000000"
        recommendations["justify"] = "center"
        recommendations["text"] = "View Recommendations"
        recommendations.place(x=320, y=300, width=200, height=33)
        recommendations["command"] = self.recommendations_button_command

    def search_button_command(self):
        book = self.search_entry.get().strip().lower()
        book_info = bs.search_book(book)
        if book_info is None:
            self.search_results["text"] = "Book not found"
        else:
            self.search_results["text"] = "Book ID: " + str(book_info[0]) + "\nTitle: " + \
                book_info[2] + "\nGenre: " + \
                book_info[1] + "\nAuthor: " + book_info[3]

    def checkout_button_command(self):
        member_id = self.memberID_entry.get()
        book_id = self.book_entry.get()
        result = bc.book_checkout(book_id, member_id)
        if result == True:
            tk.messagebox.showinfo("Success", "Book checked out")
        elif result == "Book not found":
            tk.messagebox.showinfo("Error", result)
        elif result == "Invalid member ID":
            tk.messagebox.showinfo("Error", result)
        elif result == "Book is not available":
            reserve = tk.messagebox.askyesno(
                "Question", result+".\nWould you like to reserve the book?")
            if reserve:
                status = db.reserve_book(book_id, member_id)
                if status:
                    tk.messagebox.showinfo("Success", "Book reserved")
                else:
                    tk.messagebox.showinfo("Error", "Book already reserved")

    def return_button_command(self):
        book_id = self.return_entry.get()
        result = br.return_book(book_id)
        if result == True:
            tk.messagebox.showinfo("Success", "Book returned")
        elif result == "Book has not been checked out":
            tk.messagebox.showinfo("Error", result)
        elif result == "Invalid book ID":
            tk.messagebox.showinfo("Error", result)

    def recommendations_button_command(self):
        new_window = tk.Toplevel(root)
        new_window.title("Recommendations")
        width = 900
        height = 470
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        new_window.geometry(alignstr)
        new_window.mainloop()

        return


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
