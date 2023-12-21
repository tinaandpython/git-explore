class Books:
    def __init__(self, title, author, availability):
        self.title = title
        self.author = author
        self.availability = availability

    def read_book(self):
        print(f"{self.title} by {self.author}")

    def change_availability(self):
        book_status = int(input("Status option: \n 1. Available \n 2. Borrowed \nInsert status: "))

        if book_status == 1:
            self.availability = "available"
        elif book_status == 2:
            self.availability = "borrowed"
        else:
            print("Invalid option")

    def get_availability(self):
        print(f"{self.title} by {self.author} is {self.availability}\n")


book1 = Books("Metamorphosis", "Franz Kafka", "available")
book1.read_book()
book1.change_availability()
book1.get_availability()

book2 = Books("Jane Eyr", "Charlotte Bronte", "available")
book2.read_book()
book2.change_availability()
book2.get_availability()