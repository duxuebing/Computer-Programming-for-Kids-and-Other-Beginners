# 测试题：
# 01.对于下面这行代码：answer = input() 如果用户键入12，answer会是什么数据类型？是字符串还是数字？
# 答：answer会是整数型，是数字。
# 参考答案：如果用户键入12，answer的数据类型回事字符串，因为input()总会返回一个字符串。
# 可以通过程序来验证
# print("enter a number: ", end='')
# answer = input()
# print(type(answer))

# 02.如何让input()打印一条提示消息？
# 答：
mess = input("Please enter your name ")
print(int(mess))

# 03.如何使用input()得到一个整数？
aa = int(input())
print(aa)

# # 04.如何使用input()得到一个浮点数（小数）？
bb = float(input())
print(bb)

# --------------------------------------------------------------------------------
# 动手试一试
# 01.在交互模式中创建两个变量，分别表示你的姓氏和名字。然后使用一条print()语句，把它们打印在一起。
first = 'du'
last = 'xuebing'
print(first + last)

# 02.编写一个程序，先问你的姓氏，再问你的名字，然后打印出一条消息，其中包含你的姓名。
# 答：
print("Enter your last name: ", end='')
last_name = str(input())
print("Enter your name: ", end='')
name = str(input())
print('You name is ' + last_name + name)

# 参考答案：
first = input('enter your first name: ')
last = input('enter you last name: ')
print('Hello,', first, last,'how are you today?')

# 03.编写一个程序，询问一间矩形房间的尺寸（单位是米），然后计算并显示铺满整个房间总共需要多少地毯，单位是平方米。
# 04.编写一个程序，完成第3题的要求，并且询问每平方尺地毯的价格。然后主程序显示下面3项内容。
# · 总共需要多少地毯，单位是平方米。
# · 总共需要多少地毯，单位是平方尺（1平方米=9平方尺）。
# · 地毯的总价格。
# 答：
print("Please enter length: ", end='')
Length = float(input())
print("Please enter Wide: ", end='')
Wide = float(input())
Area = Length * Wide
print('The area of the room is ' + str(Area) + ' Square meter') # 到这里我算对了

print("What is the price per square meter? ")
Price = float(input())

need_carpets = Area * Price
print("We need " + str(need_carpets) + " carpets per square meter")
need_carpets2 = (Area * 9) * Price
print("We need " + str(need_carpets2) + " carpets in square feet")
sum11 = need_carpets + need_carpets2
print("The total price of the carpet is " + str(sum11))
#------------------以上六行代码算错了，问题是将平方尺来算价格，我是将平方米和平方尺各自算了一个价格出来，再相加。。。-------------------------

# 参考答案：
length = float(input('length of the room in meter: '))
width = float(input('width of the room in meter: '))
cost_per_chi = float(input('cost per square chi: '))
area_meter = length * width
area_chi = area_meter * 9
total_cost = area_chi * cost_per_chi
print('The area is', area_meter, 'square meter.')
print('Theat is ',area_chi, 'square chi.')
print('Which will cost', total_cost)


# 05.编写一个程序，帮助用户统计一些零钱。程序要问下面的问题。· “有多少枚1分”· “有多少枚1角？”· “有多少枚1元？”让程序给出这些零钱的总值（单位是元）。
print("How many 1 points do you have? ", end='')
points = int(input())
print("How many dimes do you have? ", end='')
dimes = int(input())
print("How many 1 yuan do you have? ", end='')
yuan = int(input())
print("You have a total of " + str(yuan) + " yuan, " + str(dimes) + " cents and " + str(points) + " cents")

# 参考答案：
fen = int(input("How many fen? "))
jiao = int(input("How many jiao? "))
yuan = int(input("How many yuan? "))
total = 0.01 * fen + 0.10 * jiao + 1.00 * yuan
print("You have a total of: ", total)
















