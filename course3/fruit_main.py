from course3.Apple import Apple
from course3.Fruit import Fruit
from course3.Banana import Banana
from course3.Strawberry import Strawberry

if __name__ == "__main__":
    balance=40
    # apple=Fruit('apple',5,0)
    # banana=Fruit('banana',6,0)
    apple=Apple(5,0)
    banana=Banana(2,0)

    apple.set_price(6)
    apple.set_quantity(10)
    print(apple.eatable)
    print(apple)

    print(banana)

    strawberry=Strawberry(2,0)
    print(strawberry.has_core())
    print(strawberry)