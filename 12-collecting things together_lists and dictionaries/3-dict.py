phoneNumbers = {}  # 创建一个空字典
phoneNumbers["John"] = "555-1234"  # 添加一个元素
print(phoneNumbers)  # {'John': '555-1234'}

phoneNumbers["Mary"] = "555-6789"
phoneNumbers["Boy"] = "444-4321"
phoneNumbers["Jenny"] = "867-5309"
print(phoneNumbers)  # {'John': '555-1234', 'Mary': '555-6789', 'Boy': '444-4321', 'Jenny': '867-5309'}
print(phoneNumbers["Mary"])  # 555-6789
print(phoneNumbers.keys())  # keys() 会列出字典中所有元素的键 ，dict_keys(['John', 'Mary', 'Boy', 'Jenny'])
print(phoneNumbers.values()) # values() 则会列出字典中所有元素的值，dict_values(['555-1234', '555-6789', '444-4321', '867-5309'])

for key in sorted(phoneNumbers.keys()):
    print(key,phoneNumbers[key])
# Boy 444-4321
# Jenny 867-5309
# John 555-1234
# Mary 555-6789

print("-------------------------------------")
# 把电话号码按从小到大的顺序输出
for value in sorted(phoneNumbers.values()):
    for key in phoneNumbers.keys():
        if phoneNumbers[key] == value:
            print(key, phoneNumbers[key])

# Boy 444-4321
# John 555-1234
# Mary 555-6789
# Jenny 867-5309

# del 删除某个元素
del phoneNumbers["John"]
print(phoneNumbers)  # {'Mary': '555-6789', 'Boy': '444-4321', 'Jenny': '867-5309'}

# 使用clear() 删除所有元素（清空字典）
phoneNumbers.clear()
print(phoneNumbers)  # {}

# 使用in关键字判断字典中是否存在某个键。
phoneNumbers = {'Bob': '444-4321', 'Mary': '555-6789', 'Boy': '444-4321', 'Jenny': '867-5309'}
print("Bob" in phoneNumbers)  # True
print("Barb" in phoneNumbers)  # False
