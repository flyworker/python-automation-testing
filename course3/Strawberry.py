from course3.Fruit import Fruit
class Strawberry(Fruit):
    __name='Strawberry'
    __expire_time=30
    __has_core = False
    def __init__(self, price, quantity):
        super().__init__(self.__name, price, quantity)

    def get_price(self):
        return super().get_price()+1

    def has_core(self):
        return self.__has_core

    def __str__(self):
        return "Have %d %ss price:  %d. Has core %d "\
               %(self.get_quantity(),self.__name,
                 self.get_price(),self.has_core())