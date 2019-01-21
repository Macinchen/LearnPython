# 这个是练习 For...In 循环的

# for x in ...循环就是把每个元素代入变量x，然后执行缩进块的语句。

sum = 0 #为什么需要这句？通过这句来声明 sum 的变量类型
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)


# 能够与用户交互的求和程序：
a = int(input("您想计算从1到几的和？请输入："))
abc = 0
for x in range(a):
	abc = abc + x
print(abc+a)
