from course3.Fruit import Fruit


class Banana(Fruit):
    __name='banana'
    __expire_time=45

    def __init__(self, price, quantity):
        super().__init__(self.__name, price, quantity)

    def __str__(self):
        return "Have %d %ss price:  %d. Best to eat in %d "\
               %(self.get_quantity(),self.__name,
                 self.get_price(),self.__expire_time)