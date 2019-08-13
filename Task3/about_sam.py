#三目表达式--三元表达式（条件表达式）
# 如果条件为真，返回真，否则返回假
x = int(input("请输入第一个数："))
y = int(input("请输入第二个数："))
z = int(input("请输入第三个数："))
#写法1
print((x if (x>y) else y) if ((x if (x>y) else y) >z ) else z)
#写法2
a = (x if (x>y) else y)
print (a if (a>z) else z)
