#map()     处理序列中的每一个元素，得到的结果是一个‘列表’，该‘列表’元素个数及位置与原来的一样

#filter()  遍历序列中的每一个元素，判断每个元素得到布尔值，如果是True则留下来

people = [
    {'name': 'alex', 'age': 1000},
    {'name': 'wupei', 'age': 10000},
    {'name': 'yuanhao', 'age': 9000},
    {'name': 'RNG', 'age': 18}
]
res = list(filter(lambda p:p['age']<=18,people))
print(res)



#reduce:处理一个序列，然后把序列进行合并操作

from functools import reduce

print(reduce(lambda x,y:x+y,range(0,100),100))
print(reduce(lambda x,y:x+y,range(0,101)))