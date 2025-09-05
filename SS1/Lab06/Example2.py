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
    def __init__(self, name: str, author: Author, price: float, qty: int = 0):
        self.__name = name
        self.__author = author
        self.__price = price
        self.__qty = qty

    def getName(self) -> str:
        return self.__name

    def getAuthor(self) -> Author:
        return self.__author

    def getPrice(self) -> float:
        return self.__price

    def setPrice(self, price: float) -> None:
        self.__price = price

    def getQty(self) -> int:
        return self.__qty

    def setQty(self, qty: int) -> None:
        self.__qty = qty

    def __str__(self) -> str:
        return f"Book[name = {self.__name}, {self.__author}, price = {self.__price}, qty = {self.__qty}]"


kathySierra = Author("Kathy Sierra", "sierra@nowhere.com","f")
print(f"name: {kathySierra.getName()}, email: {kathySierra.getEmail()}, gender: {kathySierra.getGender()}")
kathySierra.setEmail("sierra@somewhere.net")
print(kathySierra)

# We need Author instances to create a Book instance
paulBarry = Author("Paul Barry", "barry@nowhere.com", "m")
kathySierra.setEmail("sierra@somewhere.net")

# Test Book's constructor and toString()
book1 = Book("Head First Python", paulBarry, 210)
print(book1)
book2 = Book("Head First Java", kathySierra, 150, 5)
print(book2)