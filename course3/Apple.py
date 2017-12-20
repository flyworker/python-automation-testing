from course3.Fruit import Fruit
class Apple(Fruit):
    __name='Apple'
    __expire_time=180

    def __init__(self, price, quantity):
        super().__init__(self.__name, price, quantity)

    def get_price(self):
        return super().get_price()+1

    def __str__(self):
        return "Have %d %ss price:  %d. Best to eat in %d "\
               %(self.get_quantity(),self.__name,
                 self.get_price(),self.__expire_time)