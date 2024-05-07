# 定义并调用函数
def printMyAddress(): # （本行及以下6行） 定义函数
    print("Warren Sand")
    print("123 Main Street")
    print("Ottawa, Ontario, Canada")
    print("K2M 2E9")
    print()
printMyAddress()

# Warren Sand
# 123 Main Street
# Ottawa, Ontario, Canada
# K2M 2E9


# 向函数传递参数
def printMyAddress(myName): # 将参数myName传入函数
    print(myName)  # 打印人名
    print("123 Main Stareet")
    print("Ottawa, Ontario, Canada")
    print("K2M 2E9")
    print()
printMyAddress("Carter Sande")  # 将Carter Sande 作为参数的值传入函数赋给其中的参数 myName

# 让函数返回一个值，使用return关键字
def calculateTax(price, tax_rate):
    taxTotal = price + (price *  tax_rate)
    return taxTotal

totalPrice = calculateTax(7.99,0.06)
print(totalPrice)  # 8.4694


def calulateTax(price, tax_rate): # (本行及以下2行) 函数计算税额，并返回总价格
    total = price + (price * tax_rate)
    return  total # 将计算结果返回到主程序
my_price = float(input("Enter a price: "))
totalPrice = calulateTax(my_price, 0.06)
print("price = ", my_price, " total price = ", totalPrice)  # 调用函数并把结果保存在变量totalPrice中
# Enter a price: 8
# price =  8.0  total price =  8.48












