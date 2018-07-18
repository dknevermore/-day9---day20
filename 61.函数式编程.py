#高阶函数  1.函数接收的参数是一个函数名   2.返回值中包含函数
#把函数当作参数传个另外一个函数
'''
def foo(n):
    print(n)

def bar(name):
    print('my name is %s'%name)

#foo(bar)     bar()函数名的内存地址
#foo(bar())   报错  因为bar()里面要加参数
foo(bar('alex'))

'''

#返回值中包含函数
def bar():
    print('from bar')
def foo():
    print('from foo')
    return bar     #返回值可以是任意函数
n = foo()
n()


def handle():
    print('from handle')
    return handle
h = handle()
h()


def test1():
    print('from test1')
def test2():
    print('from test2')
    return test1()  #代表了return test1()的返回值
                    #代表这函数在这直接运行了  函数运行不完return就没有办法执行
                    #一定要test()运行到结果 放到return 上才执行return
