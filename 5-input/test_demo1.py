print("Please enter length: ", end='')
Length = float(input())
print("Please enter Wide: ", end='')
Wide = float(input())
Area = Length * Wide
print('The area of the room is ' + str(Area) + ' Square meter') # 面积

print("What is the price per square meter? ")
Price = float(input())
need_carpets = Area * Price
print("We need " + str(need_carpets) + " carpets per square meter")

need_carpets2 = (Area * 9) * Price
print("We need " + str(need_carpets2) + " carpets in square feet")

sum11 = need_carpets + need_carpets2

print("The total price of the carpet is " + str(sum11))