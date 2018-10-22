import numpy as np
from matplotlib import pyplot

def define_row():
    row_num = input("How many Row and Column ?: ")
    return int(row_num)

def define_mat(row_num,mat,ans):
    for row in range (row_num):
        for column in range (row_num):
            mat[row,column]=input("what is mat("+str(row+1)+","+str(column+1)+")`s number? : ")
        ans[row]=input("\nwhat is ans(1,"+str(row+1)+")`s number? : ")
        print("")

def guess_ans(x,row_num):
    for i in range(row_num):
        sc = ans[i]
        for k in range(row_num):
            if i != k:
                sc -=mat[i,k]*x[k]
        x[i] =  sc/mat[i,i]
    return x

times = 100
flag = 0
x=[]
x_axis=[]
row_num=define_row()
mat = np.zeros((row_num,row_num))
x_plot=np.zeros((row_num,times))
ans = np.zeros(row_num)
define_mat(row_num,mat,ans)
for i in range(row_num):
    x.append(0)
for round_num in range(times):
    x = guess_ans(x,row_num)
    print("----round"+str(round_num)+"----"+str(x))
    x_axis.append(round_num)
    for k in range(row_num):
        x_plot[k,round_num]=x[k]
    if x_plot[0,round_num]==x_plot[0,round_num-1] and round_num != 0:
        flag+=1
    else: flag = 0
if flag >= 3:
    print("convergence!!\n-------round"+str(times-flag-1)+"--------")
else: print("not convergence") 
print(x,mat)
for i in range(row_num):pyplot.plot(x_axis,x_plot[i],label="x"+str(i+1))
pyplot.legend()
pyplot.show()
