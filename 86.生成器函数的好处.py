# def product_baozi():
#     ret = []
#     for i in range(100):
#         ret.append('包子%s' %i)
#     return ret
# baizi_list=product_baozi()
# print(baizi_list)

def product_baozi():
     for i in range(100):
        print('正在生产包子')
        yield '包子%s' %i    #  yield 可以保留函数的运行状态
        print('开始卖包子')
pro_g=product_baozi()

baozi=pro_g.__next__()
#加代码
baozi1=pro_g.__next__()

print('来了一个人吃包子',baozi1)

# baozi2=pro_g.__next__()
# print('来了一个人吃包子',baozi2)