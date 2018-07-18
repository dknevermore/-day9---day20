'''
num_l = [1,2,3,100]
res = 0
for num in num_l:
    res += num

print(res)

'''

# num_l = [1,2,3,100]
#
# def reduce_test(array):
#     res = 0
#     for num in array:
#         res += num
#     return res
#
# res =reduce_test(num_l)
# print(res)

'''
num_l = [1,2,3,100]

# def multi(x,y):
#     return x*y
#lambda x,y:x*y

def reduce_test(func,array,init=None):
    if init is None:
        res = array.pop(0)
    else:
        res = init
    for num in array:
        res = func(res,num)
    return res
res = reduce_test(lambda x,y:x*y,num_l,100)
print(res)

'''

#reduce函数 把所有的数据压缩到一起得到最终的结果

from functools import reduce

num_l = [1,2,3,100]

reduce(lambda x,y:x+y,num_l,1)
res = reduce(lambda x,y:x+y,num_l,1)
print(res)


#map函数 装1个列表，按照列表依次处理列表每一个元素，最终得到的还是一个列表，跟原来的列表的顺序
#是一模一样的，只不过每一个元素被处理了一遍

#filter函数 把列表当中所有的值都筛选一遍，最后得一个列表


