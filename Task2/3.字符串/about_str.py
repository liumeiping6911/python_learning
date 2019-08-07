#字符串是 Python 中最常用的数据类型。我们可以使用引号('或")来创建字符串。
#创建字符串很简单，只要为变量分配一个值即可。例如：
#Python访问子字符串，可以使用方括号来截取字符串
a = 'hello'
b = 'lmp'
print(a,b)
print("a[0]=",a[0])
print("a[0:3]=",a[0:3])

#Python字符串运算符

#python 字符串操作常用操作，如字符串的替换、删除、截取、赋值、连接、比较、查找、分割等
#1、去除空格 str.strip()：删除字符串两边的指定字符，括号的写入指定字符，默认为空格
a='    hello    '
b=a.strip()
print("***********")
print(b)
print(a.lstrip(),'123')
print(a.rstrip(),'123')

#2、连接字符串
# + 字符串连接   a + b  'HelloPython'
#注：此方法又称为 "万恶的加号",因为使用加号连接2个字符串会调用静态函数string_concat(register PyStringObject *a ,register PyObject * b),在这个函数中会开辟一块大小是a+b的内存的和的存储单元，然后将a,b字符串拷贝进去。如果是n个字符串相连  那么会开辟n-1次内存，是非常耗费资源的。
print(a+b)

# * 重复输出字符串   a * 2  'HelloHello'
print((a+b, )* 3)
# r/R  原始字符串   print r'\n'   \n
print (r'\n')
print (R'\n')

li = ["alex", "eric"]
s = "******".join(li)
print(s)


#3.查找字符串
#str.index 和str.find 功能相同，区别在于find()查找失败会返回-1，不会影响程序运行。一般用find!=-1或者find>-1来作为判断条件。
#str.index:检测字符串中是否包含子字符串str，可指定范围
a='hello world'
print(a.index('o'))
#str.find:检测字符串中是否包含子字符串str，可指定范围
b='hello world'
print(b.find('o'))

#4.in |not in
print('hello' in a)
print('helloy' in a)

#5.大小写转换、大小写互换、首字母大写
print(a.lower())
print(a.upper())
print(a.swapcase())
print(a.capitalize())

#6.将字符串放入中心位置可指定长度以及位置两边字符
print (a.center(20,'*'))
print(a.count('l'))

#7.替换
s="alex SB alex"
print(s.replace("al","SB"))


s="alex | alex"
ret = s.partition('|')
print(ret)




print("***********")

#字符串格式化
print ("My name is %s and weight is %d kg!" % ('Zara', 21) )
#常见的占位符有：%d 整数 %f 浮点数 %s 字符串 %x 十六进制整数
print('%.2f' % 3.1415926)
#
print(u'中文'.encode('gb2312') )
print('中文'.encode('gb2312') )

print('growth rate: %d %%' % 7)