#遍历字典键值对
usr_0 = {
    '1':'maomao',
    '2':'taotao',
    '3':'sansan',
}

for key , value in usr_0.items():
    print("\nKey: " + key)
    print("Value: " + value)
#遍历字典键
for name in usr_0.keys():
    print ("\n name: " + name.title())
#遍历字典值
for name in usr_0.values():
    print ("\n name: " + name.title())