# 测试题
# 01.用哪些方法可以在列表中添加元素？
# 答：append() extend() insert()

# 02.用哪些方法可以从列表中删除元素？
# 答：del() pop() remove()

# 03.用哪两种方法既可以得到列表的有序副本，又不改变原来的列表？
# 参考答案：
# 1、用分片操作符创建出列表的一个副本：
# new_list = my_list[:]。然后对新的副本列表进行排序 new_list.sort()
# 2、用sorted() 函数直接进行排序：new_list = sorted(my_list)

# 04.如何判断列表中是否存在某个值？
# 答：for x in list：

# 05.如何确定某个值在列表中的位置？
# 答：使用index()

# 06.什么是元组？
# 参考答案：元组与列表类似的集合，只不过元组不能修改。元组是不可改变的，而列表是可以改变的。

# 07.如何创建表格？
# 答：1、使用嵌套的中括号：table = [['a','b','c'],['1','2','3']]
# 2、使用append() 方法追加一个列表
# my_list = []
# my_list.append([1,2,3])
# my_list.append(['a','b','c'])
# print(my_list)
# 3、先创建单个列表，再把这些列表合并起来
# list1 = [1,2,3]
# list2 = ['a','b','c']
# my_list = [list1,list2]
# print(my_list)

# 08.如何从表格中读取某个值？
# 答：print(table[0])
# print(table[0][1])

# 09.Python中的字典是什么？
# 字典是键-值对的集合

# 010.如何在字典中添加某个元素？
# phoneNumbers["John"] = "555-1234"

# 011.如何用键查找字典中的某个元素？
# print(phoneNumbers["John"])


# 动手试一试
# 01.编写一个程序，让用户输入5个名字。该程序要把这5个名字保存在一个列表中，然后打印出来，如下所示。
# Enter 5 names:
# Tony
# Paul
# Nick
# Michel
# Kevin
# The names are ['Tony', 'Paul', 'Nick', 'Michel', 'Kevin']
# name_list = []
# print("Enter 5 name (press the Enter key after each name): ")
# for i in range(5):
#     name = input()
#     name_list.append(name)
#
# print("The name are", name_list)
# name_list.sort()
# print("第二小题，打印排序后的列表", name_list)
# print("第三小题，The third name you entered is: ", name_list[2])

# 02.修改第1题中的程序，不仅要打印出原来的名字列表，还要打印出排序后的列表。

# 03.修改第1题中的程序，要求只打印出用户输入的第3个名字，如下所示。
# The third name you entered is: Nick

# 04.修改第1题中的程序，让用户替换其中的一个名字。保证用户能够随机选择要替换的名字，然后输入新的名字。最后打印出新列表，如下所示。
# Enter 5 names:
# Tony
# Paul
# Nick
# Michel
# Kevin
# The names are ['Tony', 'Paul', 'Nick', 'Michel', 'Kevin']
# Replace one name. Which one? (1-5): 4
# New name: Peter
# The names are ['Tony', 'Paul', 'Nick', 'Peter', 'Kevin']

name_list = []
print("Enter 5 name (press the Enter key after each name): ")
for i in range(5):
    name = input()
    name_list.append(name)
print("The name are", name_list)

name_list_len = len(name_list)
new_number = int(input("Replace one name. Which one? (1-5): "))
if new_number <= name_list_len:
    new_name = input("New name: ")
    name_list[new_number] = new_name
    print("The names are", name_list)
else:
    print("请输入正确的数字")

# 参考答案
nameList = []
print("Enter 5 name (press the Enter key after each name:)")
for i in range(5):
    name = input()
    nameList.append(name)
print("The names are:", nameList)
print("Replace one name. Which one? (1-5): ", end=' ')
replace = int(input())
new = input("New name: ")
nameList[replace - 1] = new
print("The names are: ", nameList)

# 05.编写一个字典程序，让用户可以在字典中添加单词和含义，还能够在其中进行查找。当字典中不存在要查找的单词时，程序要向用户提示相应的信息。当运行时，程序应该像下面这样。
# Add or look up a word (a/l)? a
# Type the word: computer
# Type the definition: A machine that does very fast math.
# Word added!
# Add or look up a word (a/l)? l
# Type the word: computer
# A machine that does very fast math.
# Add or look up a word (a/l)? l
# Type the word: qwerty
# That word isn't in the dictionary yet.

user_dictionary = {}
while 1:
    command = input(" 'a' to add word, '1' to lookup a word, 'q' to quit ")
    if command == "a":
        word = input("Type the word: ")
        definition = input("Type the definition: ")
        user_dictionary[word] = definition
        print("Word added!")
    elif command == "l":
        word = input("Type the word: ")
        if word in user_dictionary.keys():
            print(user_dictionary[word])
        else:
            print("That word isn't in the dictionary yet.")
    elif command == 'q':
        break