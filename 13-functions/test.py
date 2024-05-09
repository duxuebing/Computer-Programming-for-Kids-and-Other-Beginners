# 测试题
# 01.可以使用哪个关键字定义函数？
# def

# 02.如何调用函数？
# function()

# 03.如何向函数传递信息（参数）？
# function(name)

# 04.函数最多可以有多少个参数？
# 没有限制，但建议不超过5个

# 05.如何从函数中返回信息？
# return

# 06.在函数运行结束后，其中的局部变量会发生什么变化？
# 参考答案：当函数运行结束后，函数体中的所有局部变量都会被销毁。

# 动手试一试
# 01.编写一个函数，用大写字母打印出你的英文名字，就像这样：
# 我以为是一个很复杂的函数，结果参考答案是一组print() .# 看来我想的太复杂了。。。

# 02.定义一个函数，可以打印出全世界任何人名、住址、街道、城市、省份（州）、邮政编码和国家。（提示：这里需要7个参数。你可以把它们作为单独的参数依次传递，也可以作为一个列表整体传递。）
# 参考答案：
# 定义一个包含7个参数的函数
def printAddr(name, num, street, city, prov, pcode, country):
    print(name)
    print(num, end=' ')
    print(street)
    print(city, end=" ")
    if prov != "":
        print(", "+prov)
    else:
        print("")
    print(pcode)
    print(country)
print()
# 调用该函数并向它传递7个参数
printAddr("Sam", "45", "Main St.", "Ottawa", "ON", "K2M 2e9", "Canada")
printAddr("Jian", "64", "2nd Ave.", "Beijing", "", "235643", "China")

# 03.尝试用代码清单13-7中的例子，不过要让my_price变为全局变量，看看输出结果有什么不同。

# 04.编写一个函数，统计一堆零钱的总值，这些零钱中包括1分、1角和1元，类似于第5章“动手试一试”中的最后一个问题。这个函数应该返回这些硬币的总值，然后再编写一个程序来调用这个函数。当运行程序时，可以看到类似下面的输出结果。
# 参考答案：
def addUpChange(fen, jiao, yuan):
    total = 0.01 * fen + 0.10 * jiao + 1.00 * yuan
    return total
