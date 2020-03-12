
class LibraryItem:
    def __init__(self, **kwargs):
        print("Initializing LibraryItem")
        self.id = kwargs.pop("id")
        self.title = kwargs.pop("title")

    def print_info(self):
        print("-------- Library Item Details --------")
        print("Item ID: " + str(self.id))
        print("Title: " + self.title)


# item1 = LibraryItem(id=77, title="Python for Beginners")
# item1.print_info()


class Book(LibraryItem):
    def __init__(self, **kwargs):
        print("Initializing Book")
        self.author = kwargs.pop("author")
        self.isbn = kwargs.pop("isbn")
        super().__init__(**kwargs)

    def print_info(self):
        super().print_info()
        print("-------- Book Details --------")
        print("Author: " + self.author)
        print("ISBN: " + str(self.isbn))

    def read(self):
        print("I am reading the book \"" + self.title + "\" for you")

# b1 = Book(id=104, title="Data Visualization", author="Muller", isbn="123-1234567890")
# b1.print_info()
# b1.read()


class SoundTrack(LibraryItem):
    def __init__(self, **kwargs):
        print("Initializing SoundTrack")
        self.singer = kwargs.pop("singer")
        self.year = kwargs.pop("year")
        super().__init__(**kwargs)

    def print_info(self):
        super().print_info()
        print("-------- Sound Track Details --------")
        print("Artist: " + self.singer)
        print("Production Year: " + str(self.year))

    def play(self):
        print("I am playing track \"" + self.title + "\" for you")

# f1 = SoundTrack(id=9, title="Winds of the West", singer="Westermann", year=2007)
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

