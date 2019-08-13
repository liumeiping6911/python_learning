#set 和 dict 类似，也是一组 key 的集合，但不存储 value。由于 key 不能重复，所以，在 set 中，没有重复的 key,重复元素在 set 中自动被过滤。

s = set([1, 1, 2, 2, 3, 3])
print(s)

s1 = set({1, 1, 2, 2, 3, 3})
print(s1)
#增加减少
s.add(999)
print(s)
s.remove(999)
print(s)
# set 可以看成数学意义上的无序和无重复元素的集合，因此，两个 set 可以做数学意义上的交集、并集等操作：
y1 = set([2,3,4])
y2 = set([7,3,4])

print(y1 & y2)
print(y1 | y2)