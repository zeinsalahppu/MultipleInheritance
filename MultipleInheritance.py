
class LibraryItem:
    def __init__(self, **kwargs):
        print("Initializing LibraryItem")
        self.id = kwargs["id"]
        self.title = kwargs["title"]

    def print_info(self):
        print("-------- Library Item Details --------")
        print("Item ID: " + str(self.id))
        print("Title: " + self.title)


# item1 = LibraryItem(77, "Python for Beginners")
# item1.print_info()


class Book(LibraryItem):
    def __init__(self, **kwargs):
        print("Initializing Book")
        super().__init__(**kwargs)
        self.author = kwargs["author"]
        self.isbn = kwargs["isbn"]

    def print_info(self):
        super().print_info()
        print("-------- Book Details --------")
        print("Author: " + self.author)
        print("ISBN: " + str(self.isbn))

    def read(self):
        print("I am reading the book \"" + self.title + "\" for you")

# b1 = Book(104, "Data Visualization", "Muller", 123-1234567890)
# b1.print_info()
# b1.read()


class SoundTrack(LibraryItem):
    def __init__(self, **kwargs):
        print("Initializing SoundTrack")
        super().__init__(**kwargs)
        self.singer = kwargs["singer"]
        self.year = kwargs["year"]

    def print_info(self):
        super().print_info()
        print("-------- Sound Track Details --------")
        print("Artist: " + self.singer)
        print("Production Year: " + str(self.year))

    def play(self):
        print("I am playing track \"" + self.title + "\" for you")

# f1 = SoundTrack(9, "Winds of the West", "Westermann", 2007)
# f1.print_info()
# f1.play()


class AudioBook(Book, SoundTrack):
    def __init__(self, id, title,  author, isbn, singer, year):
        print("Initializing AudioBook")
        super().__init__(id=id, title=title, author=author, isbn=isbn, singer=singer, year=year)

    def print_info(self):
        super().print_info()


ab1 = AudioBook(54, "Happy Farmer", "Sandy", "333-47538745", "Sally", 2010)
print(AudioBook.mro())