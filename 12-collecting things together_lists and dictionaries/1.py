friends = [] # 新建一个空列表
friends.append('David') # 在列表种添加一项David
print(friends)

friends.append('Mary')
print(friends)

# 列表可以包含任何内容
# my_list = [5, 10, 23.76, 'Hello', myTeacher, 7, another_list]

letters = ['a', 'b', 'c', 'd', 'e']
print(letters[0])  # a
print(letters[3])  # d
print(letters[1:4])  # ['b', 'c', 'd']

# 关于列表分片，还有一个重点需要记住：在执行列表分片时，所获取的其实是另一个列表，这个新列表的元素通常相对更少。这个新列表叫作原列表的一个分片，而原列表并没有改变，因此这个分片就是原列表的局部副本。
print(type(letters[1]))  # <class 'str'>
print(type(letters[1:2]))  # <class 'list'>

# 分片简写
print(letters[:2])  # ['a', 'b']
print(letters[2:])  # ['c', 'd', 'e']

# 修改元素
letters[2] = 'z'
print(letters)  # ['a', 'b', 'z', 'd', 'e']

letters[2] = 'c'
print(letters)  # ['a', 'b', 'c', 'd', 'e']

# letters[5] = 'f' # 输入不存在的索引添加，会报错
# Traceback (most recent call last):
#   File "C:\Users\duxuebing\pythonProject\Computer-Programming-for-Kids-and-Other-Beginners\12-collecting things together_lists and dictionaries\1.py", line 26, in <module>
#     letters[5] = 'f'
#     ~~~~~~~^^^
# IndexError: list assignment index out of range


# 向列表种添加元素的其他方法
# append() 在列表末尾添加元素
# extend() 在列表末尾添加多个元素
# insert() 在列表的某个位置插入元素，不一定是在列表的末尾。可以指定insert()添加元素的位置。

letters.append('n')
print(letters)  # ['a', 'b', 'c', 'd', 'e', 'n']

letters.extend(['p','q','r'])
print(letters)  # ['a', 'b', 'c', 'd', 'e', 'n', 'p', 'q', 'r']

letters.insert(2, 'z')
print(letters)  # ['a', 'b', 'z', 'c', 'd', 'e', 'n', 'p', 'q', 'r']

#  append() 和 extend() 的区别
letters = ['a', 'b', 'c', 'd', 'e']
letters.extend(['f', 'g', 'h'])
print(letters)  # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

letters = ['a', 'b', 'c', 'd', 'e']
letters.append(['f', 'g', 'h'])
print(letters)  # ['a', 'b', 'c', 'd', 'e', ['f', 'g', 'h']]

# 从列表中删除元素
letters = ['a', 'b', 'c', 'd', 'e']
letters.remove('c')
print(letters)  # ['a', 'b', 'd', 'e']

# letters.remove('f')  # 删除列表中不存在的元素，会报错
# Traceback (most recent call last):
#   File "C:\Users\duxuebing\pythonProject\Computer-Programming-for-Kids-and-Other-Beginners\12-collecting things together_lists and dictionaries\1.py", line 67, in <module>
#     letters.remove('f')
# ValueError: list.remove(x): x not in list

# 用 del 删除元素
letters = ['a', 'b', 'c', 'd', 'e']
del letters[3]
print(letters)  # ['a', 'b', 'c', 'e']

# 用pop() 删除元素
letters = ['a', 'b', 'c', 'd', 'e']
lastLetters = letters.pop()
print(letters)  # ['a', 'b', 'c', 'd']
print(lastLetters)  # e

# 搜索列表
if 'a' in letters:
    print("found 'a' in letters")
else:
    print("didn't find 'a' in letters")

    # found 'a' in letters

# 这段代码，即使要删除的元素不在列表中，系统也不会报错。
if 'a' in letters:
    letters.remove('a')


# 查找索引
letters = ['a', 'b', 'c', 'd', 'e']
print(letters.index('d'))  # 3

if 'd' in letters:
    print(letters.index('d'))  # 3


# 循环处理列表
letters = ['a', 'b', 'c', 'd', 'e']
for letter in letters:
    print(letter)

# a
# b
# c
# d
# e


# 列表排序
letters = ['d', 'a', 'e', 'c', 'b']
print(letters)
letters.sort()
print(letters)

# ['d', 'a', 'e', 'c', 'b']
# ['a', 'b', 'c', 'd', 'e']

# 按逆序排列
letters = ['d', 'a', 'e', 'c', 'b']
letters.sort()
print(letters)
letters.reverse()
print(letters)

# ['a', 'b', 'c', 'd', 'e']
# ['e', 'd', 'c', 'b', 'a']

# 第二种方法
letters = ['d', 'a', 'e', 'c', 'b']
letters.sort(reverse=True)
print(letters)  # ['e', 'd', 'c', 'b', 'a']


original_list = ['Tom', 'James', 'Sarah', 'Fred']
new_list = original_list[:]
new_list.sort()
print(original_list)
print(new_list)

# ['Tom', 'James', 'Sarah', 'Fred']
# ['Fred', 'James', 'Sarah', 'Tom']

# 另外一种排序方法：sorted()
original = [5,2,3,1,4]
newer = sorted(original)
print(original)
print(newer)

# [5, 2, 3, 1, 4]
# [1, 2, 3, 4, 5]

