'''
def test():
    pass
print(test)   #函数名对应的内存地址

def test1():
    print('aaaaaaaaa')
def test():
    print("6666666")
    return test1

res = test()
print(res())  #test1()
'''

'''
name = 'alex'
def foo():
    name = 'lhf'
    def bar():              #加载到内存什么都不干
        #name = "我好帅"
        print(name)
    return bar
a = foo()
print(a)
a()    #bar()
'''

''''

name='alex'

def foo():
    name='lhf'
    def bar():
        name='wupeiqi'
        def tt():
            print(name)
        return tt
    return bar

func  =foo()    #foo()  ==> bar
func()()        #bar() ==> tt
                #tt()  ==> print(name)

#直接   tt()是会报错的   因为  tt() 局部作用域

'''