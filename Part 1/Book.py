class Book:

    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")

    __booklist = None

    def __init__(self, title, author, pages, price, booktype):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        if not booktype in Book.BOOK_TYPES:
            raise ValueError(f"{booktype} is not a valid book type.")
        else:
            self.booktype = booktype


    @classmethod
    def getbooktypes(cls):
        return cls.BOOK_TYPES

    @staticmethod
    def getbooklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist

    def getPrice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def setTitle(self, newtitle):
        self.title = newtitle

    def setdiscount(self, amount):
        self._discount = amount


# Create some book instances
bookone = Book("1984", "George Orwell", 328, 14.99, "EBOOK")
booktwo = Book("Animal Farm", "George Orwell", 126, 29.99, "PAPERBACK")


print(f"Book Types: {Book.getbooktypes()}")
print(f"The book {bookone.title} has the format {bookone.booktype}")

allbooks = Book.getbooklist()
allbooks.append(bookone)
allbooks.append(booktwo)
print(allbooks)
