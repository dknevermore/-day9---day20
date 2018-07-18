import time
#装饰器的架子
# def timmer(func):   #func=test
#     def wrapper(name,age):
#         start_time=time.time()
#         res = func(name,age)   #就是在运行test()
#         stop_time=time.time()
#         print('运行时间是%s' %(stop_time-start_time))
#         return res
#     return wrapper
#
# @timmer  # test = timmer(test)
# def test(name,age):
#     time.sleep(3)
#     print('test函数运行完毕, 名字是%s 年龄是%s' %(name,age))
#     return '哈哈哈哈哈'


#
# res = test('南神',18)   #就是在运行wrapper
# print(res)

#*****************************************************************************
#*****************************************************************************


#装饰器加参数 2.0
def timmer(func):   #func=test
    def wrapper(*args,**kwargs):
        start_time=time.time()
        res = func(*args,**kwargs)   #就是在运行test()
        stop_time=time.time()
        print('运行时间是%s' %(stop_time-start_time))
        return res
    return wrapper

@timmer  # test = timmer(test)
def test(name,age,gender):
    time.sleep(3)
    print('test函数运行完毕, 名字是%s 年龄是%s  性别%s' %(name,age,gender))
    return '哈哈哈哈哈'
res = test('南神',18,'male')   #就是在运行wrapper
print(res)



def test2(name,age,gender): #test2(*('alex',18,'male','x','y'),**{})
    #name,age,gender=('alex',18,'male','x','y')
    print(name)
    print(age)
    print(gender)


def test1(*args,**kwargs):
    test2(*args,**kwargs) #args=*('alex',18,'male','x','y') kwargs={}

test1('alex',18,'male')