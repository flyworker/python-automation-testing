class Person:
    __name = None
    __age = None
    paid = False

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    # def setPaid(self, ispaid):
    #     self.paid = ispaid
    #


if __name__ == "__main__":
    jim = Person("Jim", 33)

    print(jim.get_name())
    print(jim.get_age())
    print(jim.paid)
    jim.paid = True
    print(jim.paid)

    Kris = Person("Kris", 18)
    Kris.set_age(24)
    print(Kris.get_age())  # 24
