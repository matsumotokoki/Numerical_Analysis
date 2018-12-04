import math
from matplotlib import pyplot as plt

EPS  = 0.1**(20)
flag = False
ans  = []
count=0

# def f(x):
#     return x**3-5*x**2-48*x+108
# def df(x):
#     return 3*x**2-10*x-48

def f(x):
    return x**3+x**2
def df(x):
    return 3*x**2+2*x

# def f(x):
#     return x**2-2*x-8
# def df(x):
#     return 2*x-2

# def f(x):
#     return x**2+10*x+9
# def df(x):
#     return 2*x+10

# def f(x):
#     return x**3+3*x**2-88*x-180
# def df(x):
#     return 3*x**2+6*x-88

# def f(x):
#     return x**3+4*x**2-31*x-70
# def df(x):
#     return 3*x**2+8*x-31

RANGE=int(input("how long are search renge? : "))
STEPS=int(input("how long are search steps? : "))
# RANGE = 100
# STEPS = 3
for x in range(-RANGE,RANGE,STEPS):
    print("start :"+str(x))
    c=0
    x_axis = []
    x_plot = []
    while True:
        if df(x)!=0:
            x -=f(x)/df(x)
            print ("---round---"+str(c+1)+" : "+str(x))
            x_axis.append(c)
            x_plot.append(x)
            c+=1
        else:
            flag=True
            break
        if abs(f(x))<EPS:
            break
    if len(ans)==0:
        ans.append(x)
    else:
        for i in range(len(ans)):
            if ans[i] == x:
                flag = True
        if flag==False:
            ans.append(x)
        flag=False
    plt.plot(x_axis,x_plot)
    print()

print ("finish\nanser is "+str(ans))
plt.show()
