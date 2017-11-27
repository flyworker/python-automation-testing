a=3
b=4
c=5

y=10
# for  y accuracy 0.1%,  find x

# 1. how do you know x range
# 2. less steps no more than 10000
for x in range(-10,10):
    y=a*x*x+b*x+c
    print(x,y)