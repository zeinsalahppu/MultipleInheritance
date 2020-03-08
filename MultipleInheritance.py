
class LibraryItem:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def print_info(self):
        print("Item ID: " + str(self.id))
        print("Title: " + self.title)


class Book(LibraryItem):
    def __init__(self, id, title, author, isbn):
        LibraryItem.__init__(self, id, title)
        self.author = author
        self.isbn = isbn

    def read(self):
        print("I am reading the book \"" + self.title + "\" for you")

b1 = Book(104, "Data Visualization", "Muller", 123-1234567890)
b1.read()
print(b1.author)
print(b1.title)
b1.print_info()


