#Python 内置了字典：dict 的支持，dict 全称 dictionary，在其他语言中也称为 map，使用键-值（key-value）存储，具有极快的查找速度
#1访问字典中的值
alien_0 = {'color':'green','points':5,'languages':'yelu','speed':'medium'}
print(alien_0['languages'])
print(alien_0['color'])
print(alien_0['points'])
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

#2.添加键—值对。Python不关心键—值对的添加顺序， 而只关心键和值之间的关联关系,使用字典来存储用户提供的数据或在编写能自动生成大量键—值对的代码时，通常都需要先 定义一个空字典
print(alien_0)
alien_0['x_position']='0'
alien_0['y_position']='25'
print(alien_0)

#3.修改字典的值
alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
print("Original x_position:" + str(alien_0['x_position']))

if alien_0['speed']=='slow':
    x_increment = 1
elif alien_0['speed']=='medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position']= alien_0['x_position'] + x_increment

print("new x_position: " + str(alien_0['x_position']))

#4删除键—值对
alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
print("***************" )
print(alien_0)
del alien_0['x_position']
print(alien_0)

#5.由类似对象组成的字典
favorite_languaes = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
}
print(favorite_languaes)
print("Sarah's favorite language is " +
      favorite_languaes['sarah'].title()+
      ".")