#什么是生成器？
#可以理解为一种数据类型，这种数据类型自动实现了迭代器协议(其他的数据类型需要调用自己内置的__iter__方法)，所以生成器就是课迭代对象


#生成器的分类及在python中的表现形式：（Python有两种不同的方式提供生成器）
#1.生成器函数：常规函数定义，但是，使用yield语句而不是return语句返回结果。yield语句一次返回一个结果，
#在每个结果中间，挂起函数的状态，以便下次从它离开的地方继续执行
#2.生成器表达式：类似于列表推导，但是，生成器返回按需产生结果的一个对象，而不是一次构建一个结果列表


#为何使用生成器和生成器的优点
#Python使用生成器对延迟操作提供了支持。所谓延迟操作，是指在需要的时候才产生结果，而不是立即产生结果。这也是生成器的主要好处


#生成器小结：
#1.是可迭代对象
#2.实现了延迟计算，省内存啊
#3.生成器本质和其他的数据类型一样，都是实现了迭代器协议，只不过生成器附加了一个延迟计算省内存的好处，
#其余的可迭代对象可没有这点好处，记住喽！！！

'''

def test():
    yield 1
    yield 2
    yield 3
g = test()
print('来自函数',g)
print(g.__next__())
print(g.__next__())

'''

'''
#*****三元表达式*************
name = 'alex'
#name = 'linhaifeng
res = 'SB' if name == 'alex' else '帅哥'
print(res)

'''


#列表解析
# egg_list = []
# for i in range(10):
#     egg_list.append('鸡蛋%s' %i)
# print(egg_list)

l = ['鸡蛋%s' %i for i in range(10)]  #列表解析 会真实存在内存 所以在处理大数据的时候会占内存
print(l)
# l1 = ['鸡蛋%s' %i for i in range(10) if i > 5]  #列表解析 加三元表达式
# print(l1)
# #l2 = ['鸡蛋%s' %i for i in range(10) if i > 5 else i]  #没有四元表达式
# l2 = ['鸡蛋%s' %i for i in range(10) if i < 5 ]
# print(l2)

laomuji = ('鸡蛋%s' %i for i in range(10))  #生成器表达式
print(laomuji)
print(laomuji.__next__())
print(laomuji.__next__())
print(laomuji.__next__())
print(next(laomuji))

#总结

#1.把列表解析的[]换成()得到的就是生成器的表达式

#2.列表解析与生成器的表达式都是一种便利的编程方式，只不过生成器表达式更节省内存

#3.Python不但使用迭代器协议让for循环变得更加通用。大部分内置函数，也是使用迭代器协议访问对象的。
#例如，sum函数是python的内置函数，该函数使用迭代器协议访问对象，而生成器实现了迭代器协议。
#所以，我们可以直接这样计算一系列值的和：
# sum(x**2 for x in range(4))
#而不用多此一举的先构造一个列表
# sum([x**2 for x in range(4)]）
