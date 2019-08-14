with open('/python_learn/untitled/Task4/pi_digits.txt') as file_object:
    #contents = file_object.read()
    contents = file_object.readlines()
    #print(contents.st)
print("#################")
for line in contents:
    print (line.strip())
print("#################")
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

#strip()、rstrip()和lstrip()传入的是一个字符数组,依次去除。
print('  abc  '.strip())
print('  abc  '.rstrip())
print('  abc  '.lstrip())
print('wwabcbb'.strip('w'))
print('abwwabcbbab'.rstrip('ab'))
print('mississippi'.rstrip('ip'))
print('wwabcbb'.lstrip('ab'))








