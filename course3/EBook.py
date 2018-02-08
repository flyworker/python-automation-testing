from course3.Book import Book


class EBook(Book):
    # name = ""
    __price = 0
    __weight = 1.0

    def __init__(self, name, price=0, weight=1.0):
        super().__init__(name, price, weight)


    def getName(self):
        return "Ebook: "+self.name

    def __str__(self):
        return "name: %s  price: %d weight: %f" \
               % (self.name, self.__price, self.__weight)


if __name__ == "__main__":
    red_and_black = EBook("Red and Black", 4)
    print(red_and_black)
    print(red_and_black.getName())
