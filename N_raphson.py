import math

EPS  = 0.1**(20)
flag = False
ans  = []

def f(x):
    return x**3-4*x**2+x+6
def df(x):
    return 3*x**2-8*x+1

RANGE=int(input("how long are search renge? : "))
STEPS=int(input("how long are search steps? : "))
for x in range(-RANGE,RANGE,STEPS):
    while True:
        if df(x)!=0:
            x -=f(x)/df(x)
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
print(ans)
