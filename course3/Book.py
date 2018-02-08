class Book:
    name = ""
    __price = 0
    __weight = 1.0

    def __init__(self, name, price=0, weight=1.0):
        self.name = name
        self.__price = price
        self.__weight = weight

    def getName(self):
        return self.name

    def __str__(self):
        return "name: %s  price: %d weight: %f" \
               % (self.name, self.__price, self.__weight)


if __name__ == "__main__":
    red_and_black = Book("Red and Black", 4)
    print(red_and_black)
