class Fruit:
    __name=''
    __price=0
    __quantity=0

    def __init__(self,name,price,quantity):
        self.__name=name
        self.__price=price
        self.__quantity=quantity

    def get_quantity(self):
        return self.__quantity

    def get_name(self):
        return self.__name
    def get_price(self):
        return self.__price

    def set_quantity(self,quantity):
        self.__quantity=quantity

    def __str__(self):
        return "Have %d %ss price:  %d "\
               %(self.__quantity,self.__name,self.__price)
