a = 24
b = float(a)
print(a)
print(b)

c = 38.0
d = int(c)
print(c)
print(d)

print(0.1 + 0.2) #没错，Python存储的所有数字都是以二进制形式存储的。在算0.1和0.2的和时，Python会用足够多的二进制位创建一个浮点数（小数），用来保证15个小数位。不过这个二进制数并不完全等于0.3，它只是非常接近。在这里，误差是0.00000000000000004。这个误差称为舍入误差(roundoff error)。

e = 54.99
f = int(e)
print(e)
print(f)
# 54.99
# 54  尽管54.99 与55 很接近，但是得到的整数仍然是54.这是因为int()函数总是向下取整

a = '76.3'
b = float(a)
print(a)
print(b)

a = '44.2'
b = 44.2
print(type(a)) # type 函数指出变量类型
print(type(b))

print(float('fred')) # 转换类型错误


















