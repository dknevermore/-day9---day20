# num_l = [1,2,3,85,6,8,9]
# num1_l = [1,2,6,39,7,24,9]
# ret = []
# for i in num_l:
#     ret.append(i**2)
# print(ret)

'''
num_l = [1,2,3,85,6,8,9]
num1_l = [1,2,6,39,7,24,9]

def map_test(array):
    ret = []
    for i in array:
        ret.append(i**2)
    return ret

ret = map_test(num_l)
print(ret)
ret2 = map_test(num1_l)
print(ret2)

'''

'''
num_l = [1,2,3,85,6,8,9]
num1_l = [1,2,6,39,7,24,9]

#lambda x:x+1
def add_one(x):
    return x+1

#lambda x:x-1
def reduce_one(x):
    return x-1

#lambda x:x**2
def pf(x):
    return x**2

def map_test(func,array):
    ret = []
    for i in array:
        res = func(i)  #add_one(i)
        ret.append(res)
    return ret

print(map_test(add_one,num_l))
print(map_test(lambda x:x+1,num_l))
print(map_test(reduce_one,num_l))
print(map_test(lambda x:x-1,num_l))
print(map_test(pf,num_l))
print(map_test(lambda x:x**2,num_l))
'''

#终极版本

num_l = [1,2,3,85,6,8,9]

def reduce_one(x):
    return x-1

def map_test(func,array):  #func = lambda x:x+1  array = num_l
    ret = []
    for i in array:
        res = func(i)  #add_one(i)
        ret.append(res)
    return ret

print(map_test(lambda x:x+1,num_l))
res = map(lambda x:x+1,num_l)        #方法(lambda x:x+1)处理后面的可迭代对象(num_1)  for循环依次把元素赋值给方法
print("内置函数map，处理结果",res)   #map得到的结果也是可迭代对象
# for i in res:
#     print(i)
print(list(res))
print('传的是有名函数',list(map(reduce_one,num_l)))

msg = "linhaifeng"
print(list(map(lambda x:x.upper(),msg)))




