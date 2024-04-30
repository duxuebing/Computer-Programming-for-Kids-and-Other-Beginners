# 测试题

# 01.Python中的乘法使用哪个符号？
# *

# 02.Python计算9/5的结果是什么？
print(9 / 5)
# 1.8

# 03.怎么得到9/5的商？
print(9 // 5)

# 04.怎么得到9/5的余数？
print( 9 % 5)

# 05.在Python中计算6 * 6 * 6 * 6的另一种做法是什么？
print(6*6*6*6)
print(6 ** 4)

# 06.如何用E记法表示17000000 ？
# 1.7e7

# 07.如果按常规的写法（不是E记法），4.56e–5应该写成什么？
# 0.0000456

# --------------------------------------------------------------------------------

# 动手试一试
# 01.使用交互模式或者编写一个小程序来解决下面的问题。
# (a)3个人在餐厅吃饭，想分摊饭费。总共花费了35.27元，他们还想留15%的小费。每个人应付多少钱？

# 计算15%的小费是多少钱
Total_cost = 35.27
Tip = 0.15
xiaofei = Total_cost * Tip
print(xiaofei)

# 总费用 + 小费
zong = Total_cost + xiaofei
print(zong)

# 算上小费后一共需要付多少钱，再除于3，算人均
renjun = zong / 3
print(renjun)
# ---------------------------------
Total = 35.27
Tip = 0.15
people = 3
print(((Total * Tip) + Total) / people)
# --------------------------------- 最后一个是参考答案
print(35.27 * 1.15 / 3)

# (b)计算长为16.7米、宽为12.5米的矩形房间的面积和周长。
# 矩形房间面积 = 长度 * 宽度
Length = 16.7
Wide = 12.5
print(Length * Wide)
# 矩形房间周长公式 = （宽度 + 高度） * 2
print((Length + Wide) * 2)
# ------------------------------- 参考答案
length = 16.7
width = 12.5
perimeter = 2 * length + 2 * width
Area = length * width
print('Length = ', length, 'Width = ', width)
print('Area = ', Area)
print('Perimeter = ', perimeter)

# 02.编写一个程序，把温度从华氏度(F)转换为摄氏度(C)。换算公式是C = 5 / 9 * (F – 32)。
# 参考答案：
fahrenheit = 75
celsius = 5/9 * (fahrenheit - 32)
print("Fahrenheit = ", fahrenheit, "Celsius = ", celsius)

# 03.你知道怎么计算坐车去某个地方需要花多长时间吗？相应的公式可以表示成“旅行时间等于距离除以速度”。
# 参考答案：
distance = 200
speed = 80
time = distance / speed
print("time = ", time)









