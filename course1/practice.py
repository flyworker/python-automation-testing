

def three_order_eq(a,b,c,x):
    #print("y="+str(a)+"*x**3+"+str(b)+"*x+"+str(c))
    return a*x**3+b*x+c

y =100
a=2
b=3
c=1

n=100000
x=5
print("x: ",x,"y: ",three_order_eq(1,2,3,x))

for x in range(-n,n):
    x/=1000
    yx=three_order_eq(a,b,c,x)

    if yx-y<0.1 and yx-y>-0.1:
        print(x, yx-y,yx)
        break
print("End")



