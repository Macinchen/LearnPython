#允许用户输入abc三个值，再来求解
import math
def quadratic(a,b,c):
    if a == 0:
        print("x=",-c/b)
    elif b*b - 4*a*c < 0:
        print("该方程无解！")
    elif b*b - 4*a*c == 0:
        print("该方程只有一个解，x=", -b/(2*a))
    else:
        print("该方程有两个解，")
        d=b*b-4*a*c
        x1=(-b+math.sqrt(d))/(2*a)
        x2=(-b-math.sqrt(d))/(2*a)
        print("X1=",round(x1,2))
        print("X2=",round(x1,2))
a = float(input("input a:"))
b = float(input("input b:"))
c = float(input("input c:"))
print("您输入的方程为：", a,"X^2+",b,"X+",c,"=0","其答案为：")
print(quadratic(a,b,c))