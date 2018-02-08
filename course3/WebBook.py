from course3.Book import Book
from course3.EBook import EBook


class WebBook(EBook):
    # name = ""
    __price = 0
    __weight = 1.0
    __has_internet = False

    def __init__(self, name, price=0, weight=1.0, has_internet=False):
        super().__init__(name, price, weight)
        self.__has_internet = has_internet

    def __str__(self):
        if not self.__has_internet:
            return "Need Internet Access"
        else:
            return "name: %s  price: %d weight: %f" \
                   % (self.name, self.__price, self.__weight)


if __name__ == "__main__":
    red_and_black = WebBook("Red and Black", 4,has_internet=True)
    print(red_and_black)
