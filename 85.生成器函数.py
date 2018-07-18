l = [i for i in range(10)]  #列表解析
print(l)

g_l = (i for i in range(10))  #生成器表达式
print(g_l)
print(g_l.__next__())

import time
def test():          #生成器函数   yield 在上一次操作终止时 开始操作   与 return有点像
    print('开始生儿子了。。。。。。')
    print('开始生儿子了。。。。。。')
    print('开始生儿子了。。。。。。')
    yield '我'
    time.sleep(3)
    print('开始生儿子了。。。。')
    yield '儿子'
    time.sleep(3)
    print('开始生孙子了。。。。')
    yield '孙子'
    time.sleep(3)
    print('开始生重孙子了。。。。')
    yield '重孙子'
    yield 5

res = test()
print(res)
print(res.__next__())  #test()
print(res.__next__())  #test()
print(res.__next__())  #test()
print(res.__next__())  #test()