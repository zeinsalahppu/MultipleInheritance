print(__name__)

class LibraryItem:
    def __init__(self, **kwargs):
        self.id = kwargs.pop("id")
        self.title = kwargs.pop("title")

    def print_info(self):
        print("-------- Library Item Details --------")
        print("Item ID: " + str(self.id))
        print("Title: " + self.title)


class Book(LibraryItem):
    def __init__(self, **kwargs):
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


class SoundTrack(LibraryItem):
    def __init__(self, **kwargs):
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


class AudioBook(Book, SoundTrack):
    def __init__(self, id, title,  author, isbn, singer, year):
        super().__init__(id=id, title=title, author=author, isbn=isbn, singer=singer, year=year)

    def print_info(self):
        super().print_info()


def details(obj):
    obj.print_info()


if __name__ == "__main__":
    ab1 = AudioBook(54, "Happy Farmer", "Sandy", "333-47538745", "Sally", 2010)
    print(AudioBook.mro())

