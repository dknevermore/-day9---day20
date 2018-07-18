#函数嵌套
'''
def father(name):
    print('from father %s' %name)
    def son():
        print('from son')
        def grandson():
            print('from grandson')
            grandson()
        son()

father('爸爸')
'''


# def father(name):
#     #print('from father %s' %name)
#     def son():
#         print('你爸爸我是%s' %name)
#     son()
# father('杰罗姆')


#闭包
#***********闭包与作用域 是一回事**********
def father(name):
    #print('from father %s' %name)
    def son():
        #name='linhaifeng_1'
        print('我爸爸是%s' %name)
        def grandson():
            name='就是我自己'
            print('我爷爷是%s' %name)
        grandson()
    son()

father('lhf')