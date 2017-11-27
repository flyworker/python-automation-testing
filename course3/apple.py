from Fruit import Fruit

def purchase(fruit1,fruit2,init_balance):
    for count in range(0,(init_balance//fruit1.get_price())):
        balance=init_balance
        print("Round :",count+1)
        balance-=fruit1.get_price()*count
        fruit1.set_quantity(count)
        print(fruit1)

        fruit2_count=balance//fruit2.get_price()
        balance-=fruit2_count*fruit2.get_price()
        fruit2.set_quantity(fruit2_count)
        print(fruit2)

if __name__ == "__main__":
    balance=40
    apple=Fruit('banana',5,0)
    orange=Fruit('pear',6,0)

    if(apple.get_price()>orange.get_price()):
        purchase(apple,orange,balance)
    else:
        purchase(orange,apple,balance)
