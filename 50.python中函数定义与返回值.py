#   python中函数定义方法：
#
#   def test(x):
#       "The function definitions"
#       x+=1
#       return x
#
#   def:定义函数的关键字
#   test：函数名
#  （）：内可定义形参
#   "":文档描述（非必要，但是强烈建议为你的函数添加描述信息）
#   x+=1：泛指代码块或程序处理逻辑
#   return：定义返回值

def test(x):
    '''
    2*x+1
    :param x:整形数字
    :return:返回计算结果
    '''
    y = 2*x+1
    return y
print(test)
a = test(3)
print(a)


#过程：就是没有返回值的函数

def test01():
    msg='hello The little green frog'
    print(msg)

def test02():
   msg='hello WuDaLang'
   print(msg)
   return msg

t1=test01()
t2=test02()
print(t1)
print(t2)

#总结
#返回值=0，返回None
#返回值=1，返回object
#返回值=0，返回tuple


