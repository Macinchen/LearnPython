#BMI判断的程序
hight = float(input("请输入您的身高(m)："))
weight = float(input("请输入您的体重(Kg)："))
BMI = round(weight/pow(hight,2),2)  #round(x,2)保留2位小数。 pow(x,2)求x的2次方
print("您的BMI指数为：",BMI,"属于") 
if BMI >= 32:
	print ("严重肥胖")
elif BMI >= 28:
	print("肥胖")
elif BMI >= 25:
	print("过重")
elif BMI >= 18.5:
	print("正常")
else:
	print("过轻")