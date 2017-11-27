from apple import  purchase

if __name__ == "__main__":
    balance = 40
    apple = 5
    orange = 4

    if (apple > orange):
        print('Fruit 1 is apple, fruit 2 is orange.')
        purchase(apple, orange, balance)
    else:
        print('Fruit 1 is orange, fruit 2 is apple.')
        purchase(orange, apple, balance)
