# 测试题

"""
01.如何告诉Python变量是字符串（字符）而不是数字？
给字符加上双引号或单引号

02.创建一个变量之后，能不能改变赋给这个变量的值？
可以改变
例如：
name = "duxuebing"
print(name)
name = "bingxuedu"
print(name)

03.变量名TEACHER与TEACHEr相同吗？
不相同，变量名区分大小写。

04.对Python来说，'Blah'与"Blah"一样吗？
一样

05.对Python来说，'4'是不是等同于4 ？
不是，'4' 是字符串，4 是数字。

06.下面哪个变量名不正确？为什么？
(a) Teacher2
(b) 2Teacher
(c) teacher_25
(d) TeaCher
第二个变量名不正确，变量名不能用数字开头。

07."10"是数字还是字符串？
是字符串

"""

# --------------------------------------------------------------------------------

# 动手试一试
# 01.创建一个变量，并赋给它一个数值（任何数值都行）。然后使用print函数显示这个变量。
number = 123
print(number)

# 02.改变这个变量，可以用一个新值替换原来的值，或者将原来的值增加某个量。然后使用print函数显示这个新值。
number = 456
print(number)

number2 = number + 1
print(number2)

# 03.创建另一个变量，并赋给它一个字符串（某个文本）。然后使用print函数显示这个变量。
strtest = "duxuebing"
print(strtest)

# 04.像在第1章中一样，在交互模式中，让Python计算一周有多少分钟。不过，这一次要使用变量。以DaysPerWeek（每周的天数）、HoursPerDay（每天的小时数）和MinutesPerHour（每小时的分钟数）为变量名，分别创建变量（也可以自己起变量名），然后将它们相乘。
DaysPerWeek = 7
HoursPerDay = 24
MinutesPerHour = 60
WeeksMinutes = DaysPerWeek * HoursPerDay * MinutesPerHour
print(WeeksMinutes)

# 05.人们总是说没有足够的时间做到尽善尽美。如果一天有26小时，那么一周会有多少分钟呢？（提示：改变变量HoursPerDay。）
DaysPerWeek = 7
HoursPerDay = 26
MinutesPerHour = 60
WeeksMinutes2 = DaysPerWeek * HoursPerDay * MinutesPerHour
print(WeeksMinutes2)







