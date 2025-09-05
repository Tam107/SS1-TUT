class Author:
    def __init__(self, name: str, email: str, gender: str):
        self.__name = name
        self.__email = email
        self.__gender = gender

    def getName(self) -> str:
        return self.__name

    def getEmail(self) -> str:
        return self.__email

    def setEmail(self, email: str) -> None:
        self.__email = email

    def getGender(self) -> str:
        return self.__gender

    def __str__(self) -> str:
        return f"Author[name = {self.__name}, email = {self.__email}, gender = {self.__gender}]"


class Book:
    def __init__(self, name: str, authors, price: float, qty: int = 0):
        self.__name = name
        self.__authors = authors
        self.__price = price
        self.__qty = qty

    def getName(self) -> str:
        return self.__name

    def getAuthor(self) -> Author:
        return self.__authors

    def getPrice(self) -> float:
        return self.__price

    def setPrice(self, price: float) -> None:
        self.__price = price

    def getQty(self) -> int:
        return self.__qty

    def setQty(self, qty: int) -> None:
        self.__qty = qty

    def getAuthors(self) -> list:
        return self.__authors

    def getAuthorNames(self) -> str:

        return ",".join(author.getName() for author in self.__authors)

    def __str__(self):
        authors_str = ', '.join(str(author) for author in self.__authors)
        return f"Book[name = {self.__name}, {{{authors_str}}}, price = {self.__price}, qty = {self.__qty}]"



paulBarry = Author("Paul Barry", "barry@nowhere.com", "m")
authorList1 = [paulBarry]
book1 = Book("Head First Python", authorList1, 150, 5)
print(book1.getAuthorNames())

kathySierra = Author("Kathy Sierra", "sierra@nowhere.com","f")
bertBates = Author("Bert Bates", "bates@nowhere.com", "m")
authorList2 = [kathySierra, bertBates]
book2 = Book("Head First Java", authorList2, 550, 20)
print(book2.getAuthorNames())

book3 = Book("Python per tutti", [Author("Charles Severance", "sev@nowhere.com", "m"),
                                  Author("Alessandro Rossetti", "sev@nowhere.com", "m"),
                                  Author("Vittore Zen", "sev@nowhere.com", "m")], 0, 100)
print(book3.getAuthorNames())