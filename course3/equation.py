# y=a*x*x+b*x+c
# find x to make y-y1<0.1%


def calculate_x(xrange):
    loop_count = 1
    found = False
    for x in range(-xrange,xrange):
        for step_count in range(0, max_step_count):
            x1=x+ step_accuracy * step_count
            y1=a*x1*x1+b*x1+c
            loop_count+=1
            if y-y1<precision and y-y1>-precision:
                found=True
                print(x1,y1,str((y/y1-1)*100)+'%')
                print(loop_count)
                return found
    print(loop_count)
    return found

if __name__ == "__main__":
    a=3
    b=4
    c=8
    y=1000
    x=0
    precision= y*0.001
    # y=a*x*x+b*x+c
    print("Y is",y)
    step_accuracy = 0.01
    max_step_count = int(1 // step_accuracy)+1
    print(max_step_count)
    xrange=1
    xrange_step=5
    x_found=False
    while(not x_found):
        xrange=xrange*xrange_step
        print('xrange  is: ', xrange)
        for x in range(1,xrange):

            if (calculate_x(xrange)):
                x_found=True
                break