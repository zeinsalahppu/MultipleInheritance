class LibraryItem:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def print_info(self):
        print("-------- Library Item Details --------")
        print("Item ID: " + str(self.id))
        print("Title: " + self.title)


class Book(LibraryItem):
    def __init__(self, id, title, author, isbn):
        LibraryItem.__init__(self, id, title)
        self.author = author
        self.isbn = isbn

    def print_info(self):
        print("-------- Book Details --------")
        print("Author: " + self.author)
        print("ISBN: " + str(self.isbn))

    def read(self):
        print("I am reading the book \"" + self.title + "\" for you")


class SoundTrack(LibraryItem):
    def __init__(self, id, title, singer, year):
        LibraryItem.__init__(self, id, title)
        self.singer = singer
        self.year = year

    def print_info(self):
        print("-------- Sound Track Details --------")
        print("Artist: " + self.singer)
        print("Production Year: " + str(self.year))

    def play(self):
        print("I am playing track \"" + self.title + "\" for you")


class AudioBook(Book, SoundTrack):
    def __init__(self, id, title,  author, isbn, singer, year):
        Book.__init__(self, id, title, author, isbn)
        SoundTrack.__init__(self, id, title, singer, year)

print(AudioBook.mro())


ab1 = AudioBook(54,
                "Happy Farmer",
                "Sandy",
                "333-47538745",
                "Sally",
                2010)
ab1.print_info()
