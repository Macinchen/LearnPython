# 用Python写一个程序，可以自动解一元二次方程。感觉自己萌萌哒，哈哈啊哈

import math
def quadratic(a,b,c):
    if not (isinstance(a,(int,float)) and isinstance(b,(int,float)) and isinstance(c,(int,float))):
        raise TypeError('a,b,c只能为数字')
    if a==0:
        return '请输入不等于0的a值'
    else:
        d=b*b-4*a*c
        if d<0:
            return '该方程在实数域内无界'
        elif d==0:
            x=-b/(2*a)
            print("该方程的只有一解：",round(x,2))
        else:
            x1=(-b+math.sqrt(d))/(2*a)
            x2=(-b-math.sqrt(d))/(2*a)

            print("该方程的第一解为：",round(x1,2))
            print("该方程的第二解为：",round(x2,2))
            

print(quadratic(-3,4,1))