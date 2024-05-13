# 从互联网上的一个文件中获取输入
import urllib.request

file = urllib.request.urlopen('http://helloworldbook3.com/data/message.txt')
message = file.read().decode('utf-8')
print(message)

# Congratulations! You have just made your computer reach across the internet to get a secret message!
# I hope you are enjoying "Hello World! Computer Programming for Kids and Other Beginners".
# Have fun!
#
# Warren and Carter

"""
Note:

urllib.request  用于打开可扩展库
urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)
打开 url，它可以是一个包含有效的、被正确编码的 URL 的字符串，或是一个 Request 对象。 
data 必须是一个对象，用于给出要发送到服务器的附加数据，若不需要发送数据则为 None。

read()方法从文件中返回指定的字节数。默认值是-1，表示整个文件。
"""