#Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
#列出班里所有同学的名字，就可以用一个list表示
classmates = ['lili','lucy','mike']
print (classmates)

#用 len() 函数可以获得list元素的个数：
len(classmates)

#用索引来访问list中每一个位置的元素，记得索引是从 0 开始的：
print(classmates[0])
print(classmates[1])
print(classmates[2])

#当索引超出了范围时，Python会报一个IndexError错误，所以，要确保索引不要越界，记得后一个元素的索引 是 len(classmates) ‐ 1
#print(classmates[5])

#可以用 ‐1 做索引，直接获取后一个元素：
print(classmates[-1])

#list是一个可变的有序表，所以，可以往list中追加元素到末尾
classmates.append('jack')
print (classmates)

#把元素插入到指定的位置，比如索引号为 1 的位置：
classmates.insert(0,'bob')
print (classmates)

#删除list末尾的元素，用 pop() 方法：
classmates.pop()
print(classmates)

#删除指定位置的元素，用 pop(i) 方法，其中 i 是索引位置：
classmates.pop(0)
print(classmates)

#某个元素替换成别的元素，可以直接赋值给对应的索引位置：
classmates[0]='zzz'
print(classmates)

#list元素也可以是另一个list
b = ['xx','yy']
s = ['a','b',['88','99'],'c','d']
length = len (s)
print(length)
print(s[2])
print(s[2][1])

#如果一个list中一个元素也没有，就是一个空的list，它的长度为0：
m = []
length = len (m)
print("空list长度为",length)





