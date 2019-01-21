# 切片是Python的高级特性

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack'] #L为一个list

print(L[:]) 	#冒号前后都省略，则表示切取首尾
print(L[:2])	#list正数第一位为0
print(L[-2:-1])	#list倒数第一位为-1，且冒号后面为开始切的地方
print("这就是切片")

# 切片还可以针对字符串操作！所以作业来了：

#利用切片操作，实现一个trim()函数，去除字符串首尾的空格??
