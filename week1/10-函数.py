#函数就是最基本的一种代码抽象的方式。

#Python内置了很多有用的函数，我们可以直接调用。

abs() #求绝对值的函数abs
max() #求最大值
int() #转换数据类型为整型
hex() #把整数转换为十六进制数

# 自定义函数：

def my_abs(x):
	if x >= 0:
		return x
	else:
		return -x