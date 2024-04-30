# 测试题：
# 01.如何使用EasyGUI生成消息框？
# 答：easygui.msgbox("Hello there!")

# 02.如何使用EasyGUI获得字符串输入（一些文本）？
# 答：
# flavor = easygui.enterbox("What is your favorite ice cream flavor?")
# easygui.msgbox("You entered " + flavor)

# 03.如何使用EasyGUI获得整数输入？
# import easygui
# flavor = easygui.enterbox("What is your favorite ice cream flavor?")
# number = int(flavor)
# easygui.msgbox("You entered " + flavor)

# 04.如何使用EasyGUI获得浮点数（小数）输入？
# import easygui
# flavor = easygui.enterbox("What is your favorite ice cream flavor?")
# number = float(flavor)
# easygui.msgbox("You entered " + flavor)

# 05.什么是默认值？给出一个可能会用到默认值的例子。
# flavor = easygui.enterbox("What is your favorite ice cream flavor?", default = 'Vanilla') # 这是默认选项
# easygui.msgbox("You entered " + flavor)

# 动手试一试
# 01.试着修改第5章中的温度转换程序，这一次不能使用input()和print()，而是用GUI来输入和输出。

# 02.编写一个程序，询问用户的姓名，然后是街道（具体到门牌号）、城市，接下来是所属省份或所属州，最后是邮政编码，所有这些信息都要放在EasyGUI对话框中。最后，这个程序要显示一个寄信格式的完整地址，如下所示。
# John Snead
# 28 Main Street
# Akron, Ohio
# 12345
