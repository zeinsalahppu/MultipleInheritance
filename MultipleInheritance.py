import LibClass

print(LibClass)

my_libraryitem = LibClass.LibraryItem(id=77, title="Python for Beginners")

my_book = LibClass.Book(id=104, title="Data Visualization", author="Muller", isbn="123-1234567890")
my_book.read()

my_soundtrack = LibClass.SoundTrack(id=9, title="Winds of the West", singer="Westermann", year=2007)
my_soundtrack.play()

my_audiobook = LibClass.AudioBook(54, "Happy Farmer", "Sandy", "333-47538745", "Sally", 2010)
LibClass.details(my_audiobook)

# print(__name__)
