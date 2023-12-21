class Books:
    def __init__(self, title, author, availability):
        self.title = title
        self.author = author
        self.availability = availability

    def read_book(self):
        return self.author + self.title

    def change_availability(self):
        book_status = int(input("Insert the status: \n 1. Available \n 2. Borrowed "))

        if book_status == 1:
            self.availability = "Available"
        elif book_status == 2:
            self.availability = "Borrowed"
        else:
            print("Invalid option")


book1 = Books("Jane Blare", "Mathew Summers", "Available")
