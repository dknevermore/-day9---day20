#1.形参变量只有在被调用时才分配内存单元，在调用结束时，即刻释放所分配的内存单元。
# 因此，形参只在函数内部有效。函数调用结束返回主调用函数后则不能再使用该形参变量

# 2.实参可以是常量、变量、表达式、函数等，无论实参是何种类型的量，
# 在进行函数调用时，它们都必须有确定的值，以便把这些值传送给形参。因此应预先用赋值，输入等办法使参数获得确定值

def calc(x,y):   # x,y  形参
    res = x**y
    return res

a = 10
b = 10
c = calc(a,b)    #a，b  实参
print(c)

def test(x,y,z):
    print(x)
    print(y)
    print(z)
#n = test(1,2,3)     位置参数 必须一一对应，缺一不可，多一也不行
n = test(y=1,z=2,x=3)  #关键字参数 无须一一对应，缺一不可，多一也不行


#位置参数必须在关键字参数左边
#test(1,y=2,3)  报错
#test(1,3,y=2)  报错
#test(1,3,z=2)  不报错
#test(1,3,z=2,y=4)  报错

def handle(x,type=None):
    print(x)
    print(type)
#handle('hello')
#handle('hello',type='sqlite')
#handle('hello','sqlite')

#参数组：**字典  *列表,元组
def test1(x,*args):   #*args 为后期扩展准备
    print(x)
    print(args)
    print(args[0])
test1(1,2,3,4,5,6)

def test2(x,*args):
    print(x)
    print(args)
    print(args[0][0])
test2(1,['x','y','z'])

def test3(x,*args):
    print(x)
    print(args)
    print(args[1])
test3(1,*['x','y','z'])

# def test4(x,**kwargs):
#     print(x)
#     print(kwargs)
#     print(kwargs[1])
# test4(1,y=2,z=3)
# #test4(1,1,1,2,2,2,3,2y=2,z=3)   #会报错
# # test4(1,y=2,z=3,z=3)  #会报错：一个参数不能传两个值


def test5(x,*args,**kwargs):
    print(x)
    print(args,args[-1])
    print(kwargs,kwargs.get('y'))

#test5(1,1,2,3,5,x=1,y=2,z=3) 会报错 因为x=1 冲突了
#test5(1,1,2,3,5,y=2,z=3)
test5(1,*[1,2,3,4,3],**{'a':1,'y':3})