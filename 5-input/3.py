print("This program converts Fahrenheit to Celsius.")
fahrenheit = float(input("Type in a temperature in Fahrenheit: ")) # 使用float(input()) 从用户那里得到温度值（华氏度）
celsius = (fahrenheit - 32) * 0.5 / 9
# print("That is ", end='')
# print(celsius, end='')
# print( " degrees Celsius.")
print("That is ", celsius, " degrees Celsius.")

# ---------------如果希望用户输入的都是整数（而不是浮点数）可以用int() 来转换-----------------

response = input("How many students are in your class: ")
numberOfStudents = int(response)
print(numberOfStudents)