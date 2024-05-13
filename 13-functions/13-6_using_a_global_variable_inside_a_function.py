def calulateTax(price, tax_rate): # (本行及以下2行) 函数计算税额，并返回总价格
    total = price + (price * tax_rate)
    return  total # 将计算结果返回到主程序

my_price = float(input("Enter a price: "))
totalPrice = calulateTax(my_price, 0.06)
print("price = ", my_price, " total price = ", totalPrice)  # 调用函数并把结果保存在变量totalPrice中

# Enter a price: 8
# price =  8.0  total price =  8.48

