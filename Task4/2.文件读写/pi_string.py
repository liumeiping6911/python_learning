#文件读取到内存中后，就可以以任何方式使用这些数据了
filename = '/python_learn/untitled/Task4/pi_digits.txt'
with open(filename) as file_object:
    contents = file_object.readlines()

pi_string = ''
for line in contents:
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))

#注意 读取文本文件时， Python将其中的所有文本都解读为字符串。如果你读取的是数字，并
#要将其作为数值使用，就必须使用函数int()将其转换为整数，或使用函数float()将其转
#换为浮点数。

filename_1 = '/python_learn/untitled/Task4/pi_1000.txt'
with open(filename_1)  as f:
    lines = f.readlines()

pi_string_1 = ''
for line in lines:
    pi_string_1 += line.strip()

print(pi_string_1[:52] + "...")
print(len(pi_string_1))

birthday= input("enter your birthday,in the form ddyy: ")
if birthday in pi_string_1:
    print("您的生日在圆周率中")
else:
    print("不在")