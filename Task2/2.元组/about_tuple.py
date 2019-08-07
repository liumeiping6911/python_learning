#tuple
#另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名 字：
classmates = ('henly', 'lily', 'susan')
print(classmates)
print(classmates[1])

#空tuple
t = ()
print(t)

#要定义一个只有1个元素的tuple
y = (1,)
print(y)

#元组不可变，说的是指向不变，内容当元组包含列表时，列表内容改变，元组内容也变
t = ('a', 'b', ['A', 'B'])
print(t)
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)

