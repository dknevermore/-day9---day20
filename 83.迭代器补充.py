#迭代器就是可迭代对象

l = ['die','erzi','sunzi','chongsunzi']

iter_l = l.__iter__()  #iter_l ==>迭代器
# print(iter_l.__next__())
# print(iter_l.__next__())
# print(iter_l.__next__())
# print(iter_l.__next__())

print(next(iter_l))  #next()----->iter_l.__next__()
print(next(iter_l))
print(next(iter_l))
print(next(iter_l))