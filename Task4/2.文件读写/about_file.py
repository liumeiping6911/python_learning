#要以读文件的模式打开一个文件对象，使用 Python 内置的 open()函数，传入文件名和标示符：
#f = open('/Users/liume/Documents/test.txt', 'r')
#如果文件打开成功，接下来，调用 read()方法可以一次读取文件的全部内容，
#f.read()
# Python 把内容读到内存，用一个 str 对象表示：文件使用
# 完毕后必须关闭，调用 close()方法因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的：
#f.close()

f = open('/python_learn/untitled/Task4/test.txt', 'r', encoding='gbk')
y = f.read()
print(y)
f.close()

#Python 引入了 with 语句来自动帮我们调用 close()方法：
#with open('/python_learn/untitled/Task4/test.txt', 'r', encoding='gbk') as f:
#    print(f.read())

#调用 read()会一次性读取文件的全部内容,可以反复调用 read(size)方法，每次最多读取size 个字节的内容,控制
print("*************************")
with open('/python_learn/untitled/Task4/test.txt', 'r', encoding='gbk') as f:
    print(f.read(6))
print("########################")
with open('/python_learn/untitled/Task4/test.txt', 'r', encoding='gbk') as f:
    for line in f.readlines():
        print(line.strip())

print("########################")
with open('/python_learn/untitled/Task4/test123-8.txt', 'w',encoding='UTF-8') as f:
    f.write('hello,good morning')
with open('/python_learn/untitled/Task4/test123-8.txt', 'r') as l:
    print(l.read())

