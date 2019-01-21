# input数据的转换以及if判断

s = input("请输入您的出生年份：")
year = int(s)

if year >= 2000:
	print("恭喜您，您是00后！")
else:
	print("很遗憾，您已经老了！")