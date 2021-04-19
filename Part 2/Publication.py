class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price

class Periodical(Publication):
    def __init__(self, title, price, publisher, period):
        super().__init__(title, price)
        self.period = period
        self.publisher = publisher

class Book(Publication):
    def __init__(self, title, author, pages, price):
        super().__init__(title, price)
        self.author = author
        self.pages = pages

class Magazine(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, publisher, period)

class Newspaper(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, publisher, period)


book = Book('1984', 'George Orwell', 200, 29.99)
newspaper = Newspaper("LA Times", "Los Angeles Times Co", 5.99, "daily")
magazine = Magazine("Thrasher", "Thraher Mag", 10.99,  "monthly")


print(f"{magazine.title} costs {magazine.price}")

































# Create a newspaper instance
newspaper = Newspaper("LA Times", "Los Angeles Times Company", 5.99, "daily")

# Create a magazine instance
magazine = Magazine("Thrasher", "Thrasher Mag", 10.99, "Monthly")