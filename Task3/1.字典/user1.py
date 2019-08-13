#遍历字典
usr_0 = {
    's':'maomao',
    'a':'taotao',
    'c':'sansan',
}

for k , v in usr_0.items():
    print("\nKey: " + k)
    print("Value: " + v)
#遍历字典-按字母排序
for name in sorted(usr_0.keys()):
    print("key : " + name.title())
