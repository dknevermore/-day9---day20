#全局变量 与 局部变量

'''
name = 'alex'

def change_name() :
    #name = 'lhf'
    global name
    name = 'lhf'
    print(name)

    def foo():
        name = 'wu'
        print(name)

    foo()

change_name()
'''

name = 'alex'

def change_name() :
    name = 'aaaaaaa'
    print(name)

    def foo():
        nonlocal name   #nonlocal 上一级
        name = 'bbbbbbbb'
        print(name)
    print(name)
    foo()
    print(name)

change_name()