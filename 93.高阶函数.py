'''
高阶函数的定义：
1.函数接收的参数是一个函数名
2.函数的返回值是一个函数名
3.满足上述条件任意一个，都可称之为高阶函数
'''

# import time
# def foo():
#     time.sleep(3 )
#     print('你好')
# def test(func):
#     print(func)
#     start_time = time.time()
#     func()
#     stop_time = time.time()
#     print('函数运行时间是 %s' %(stop_time - start_time))
# test(foo)

'''
def foo():
    print('from the foo')
def test(func):
    return func
# res = test(foo)
# print(res)
# res()

foo = test(foo)
print(foo)
foo()
'''
# import time
# def foo():
#     time.sleep(3)
#     print('来自foo')

#不修改foo源代码
#不修改foo调用方式

#多运行了一次，不合格
# def timer(func):
#     start_time = time.time()
#     func()
#     stop_time = time.time()
#     print('函数运行时间是 %s' %(stop_time - start_time))
#     return func
# foo = timer(foo)
# foo()

#高阶函数的总结
#1.函数接收的参数是一个函数名
#  作用：在不修改函数源代码的前提下，为函数添加新功能
#  不足：会改变函数的调用方式

#2.函数的返回值是一个函数名
#  作用：不修改函数的调用方式
#  不足：不能添加新功能