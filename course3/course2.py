# we have 10 dollar in accout, apple is 5 ,
# banana is 6, check if we could buy both

# Question L. why buy apple first?
# 2.decide how many we can buy smart
# 3. maxumized the usage of the fund.
from random import randint


def purchase(product_name, balance, price, quantity):
    balance -= price
    quantity = quantity + 1
    print('Balance is', balance, 'Purchased', product_name, quantity)
    return balance, quantity


def buy(choice_list, balance, price):
    if balance <= 0:
        print('No sufficient fund.')

    else:
        for choice in choice_list:
            if choice =="apple":
                balance -= price
                print('Balance is', balance, 'Purchased', choice, 1)
                return buy(choice_list, balance, price)
            elif choice =="banana":
                print('Balance is', balance, 'Purchased', choice, 1)
                return buy(choice_list, balance, price)


if __name__ == "__main__":
    balance = 30
    apple_price = 3
    banana_price = 4
    apple_quantity = 0
    banana_quantity = 0
    choice_list = ['apple', 'banana']

    buy(choice_list, balance, apple_price)

    print('Final balance is', balance, 'Banana', banana_quantity, 'Apple', apple_quantity)
