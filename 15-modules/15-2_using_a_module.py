import my_module  # my_module 模块包含c_to_f() 函数

celsius = float(input("Enter a temperature in Celsius: "))
fahrenheit = my_module.c_to_f(celsius)
print("That's", fahrenheit, "degrees Fahrenheit")

# Enter a temperature in Celsius: 34
# That's 93.2 degrees Fahrenheit