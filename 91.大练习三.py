#1.列举布尔值为False的值
# 0 False '' [] () {} None

#2.写函数
#根据范围获取其中3和7整除的所有数的和，并返回调用者：
#符合条件的数字个数以及符合条件的数字的总和 如：def func(start,end)


#3.函数的默认返回值是什么？
# None

#4.简述break / continue / return 的区别
# break 结束当前循环
# continue 结束本次循环进入下一次循环
# return 结束函数，并返回结果，默认为None

#5.函数传递参数时，是引用还是复制值？并证明
#引用

#6.简述三元运算书写格式以及应用场景
# 变量 = 值—if条件—else 值二
# 将简单的条件判断精简写


#7.简述lambda表达式书写格式以及应用场景
# 函数名 = lambda 形参:功能   不写函数名也可以
# 将简单的函数书写成匿名函数，减少代码


#8.使用set集合获取两个列表l1 = [11,22,33,] ,l2 = [22,33,44] 中相同的元素集合
# l1 = [11, 22, 33]
# l2 = [22, 33, 44]
# same=set(l1)&set(l2)
# print(same)


#9.定义函数统计一个字符串中大写字母，小写字母，数字的个数，并以字典为结果返回给调用者
#提示：可以用id进行判断

# def num(ret):
#     yy={'大写':0,'小写':0,'数字':0}
#     for i in ret:
#         i = str(i)
#         if i.isupper():
#             yy['大写']+=1
#         elif i.islower():
#             yy['小写']+=1
#         elif i.isdecimal():
#             yy['数字']+=1
#     return yy
# ret=input('>>>')
# print(num(ret)


#10.简述函数的 位置参数，关键字参数，默认参数，可变长参数的特点以及注意事项
#位置参数 ：按形参的位置传入 叫位置参数 就是普通参数
#关键字参数 ：传入实参时指定形参的值
#默认参数;形参直接指定默认值的参数
#可变长参数：*args **kwargs，一个只能接收没有位置参数的实参或参入的列表，元组，
#俩 可以接收关键字参数和字典格式

#11.检查代码，如有错误请改正（禁止运行代码）：
#a.
# def func(x,y,z):
#     print(x,y,z)
# func(1,2,3)
#输出结果为：1 2 3


#b.
# def func(x,z,y=5):
#     print(x,y,z)
# func(1,3,3)
#输出结果为：1 3 3

#d.
# def func(x,y,*z):
#     print(x,y,z)
# func(1,2,3,4,5,6)
#输出结果为：1 2 (3,4,5,6)

#e.
# def func(x,*z,**y):
#     print(x,y,z)
# func(1,2,3)
#输出结果为:  1 {} (2, 3)

#f.
# def func(x,*y,**z):
#     print(x,y,z)
# func(1,name=2,age=3)
#输出结果为：1 () {'name': 2, 'age': 3}

#g.
# def func(x,*y,**z):
#     print(x,y,z)
# func(1,2,3,4,name=2,age=3)
#输出结果为：1 (2, 3, 4) {'name': 2, 'age': 3}


#h.
# def func(x=2,*y,**z):
#     print(x,y,z)
# func(name=2,age=3)
#输出结果为：2 () {'name': 2, 'age': 3}

#13.书写输出结果（禁止运行代码）：

#a
# def func(*y,**z):
#     print(y,z)
# func(1,2,3,4,5)
#输出结果为：(1,2,3,4,5) {}

#b.
# def func(*y,**z):
#     print(y,z)
# func([1,2,3,4,5])
#输出结果为：([1, 2, 3, 4, 5],) {}

#c.
# def func(*y,**z):
#     print(y,z)
# func(*[1,2,3,4,5])
#输出结果为：(1, 2, 3, 4, 5) {}

#d.
# def func(*y,**z):
#     print(y,z)
# func(*[1,2,3,4,5],name='alex',age=19)
#输出结果为：(1, 2, 3, 4, 5) {'name': 'alex', 'age': 19}


#e.
# def func(*y,**z):
#     print(y,z)
# func(*[1,2,3,4,5],{'name':'alex','age':19})
#输出结果为：(1, 2, 3, 4, 5, {'name': 'alex', 'age': 19}) {}

#f.
# def func(*y,**z):
#     print(y,z)
# func(*[1,2,3,4,5],**{'name':'alex',"age":19})
#输出结果为：(1, 2, 3, 4, 5) {'name': 'alex', 'age': 19}

#14.书写执行结果（禁止运行代码）
# def func1(x=1,*y,**z):
#     print(x,y,z)
#     return y
#     print(x)
# def func2(arg):
#     ret = func1(name=arg)
#     print(ret)
# result = func2('Fuck')
# print(result)

#输出结果为：
# 1 () {'name': 'Fuck'}
# ()
# None


#15.书写执行结果（禁止运行代码）
# def func(arg):
#     arg.append(55)
# li = [11,22,33,44]
# func(li)
# print(li)
# li = func(li)
# print(li)
#输出结果为：
# [11,22,33,44,55]
# None


#16.书写执行结果（禁止运行代码）
# def f1(arg):
#     print(arg+100)
# def f2(arg):
#     ret = f1(arg+1)
#     print(arg)
#     print(ret)
# ret = f2(7)
# print(ret)
#输出结果为：
# 108
# 7
# None
# None

#17.简述python3 中的range 函数和 python2.7 中的range 函数有什么区别
#python3.X  range 不会生成值 只有用的时候才会生成
#python2.7  range 会直接生成一个列表，值已经生成

#18.书写执行结果（禁止运行代码）
# a = 'oldboy%'
# print(a)
# b = 'oldboy %d %%' %(12,)
# print(b)
#输出结果为：
# oldboy%
# oldboy 12 %

#19,简述对象和类的关系
#如果值是某类型，那这个值就是这个类的对象

#20.书写执行结果（禁止运行代码）
# def func(a1):
#     return a1 +100
# func = lambda a1:a1 +200
# ret = func(10)
# print(ret)
#输出结果为：210

#21.内置函数all和any 的区别
#all 是如果是空的，返回True  如果非空，全真为真否则为假
#any 是有一个为真就为真

#22.简述文件打开模式'r'和'rb'的区别
# r 是只读模式打开，默认以utf-8格式
# rb 是以二进制格式打开

#23.将字符串'老男人'转换成UTF-8编码的字节类型
# name='老男人'
# print(bytes(name,encoding='utf-8'))
# print(name.encode('utf-8'))



#24.利用内置函数将十进制数字12，分别转换成 二进制，八进制，十六进制 表示的字符串
# print(bin(12))
# print(oct(12))
# print(hex(12))

#25.简述内置函数 globals(),locals()作用
# globals() 获取所有的全局变量
# locals()  获取所有的局部变量

#26.利用内置函数 zip(),实现功能
# l1 = ['alex',22,33,44,55,66]
# l2 = ['is',22,33,44,55,66]
# l3 = ['good',22,33,44,55,66]
# l4 = ['guy',22,33,44,55,66]
#请获取字符串s ="alex_is_good_guy"
#print('_'.join(list(zip(l1,l2,l3,l4))[0]))

#27.判断输出结果是否相同？并可得到什么结论？
# def f1(arg):
#     print(id(arg))
# n = 1111111
# print(id(n))
# f1(n)
#输出的两个值是否相同 ：相同
#执行函数是调用变量值不是复制

#28.书写执行结果（禁止运行代码）
#a.
# NAELIST = ['alex','eric']
# def func():
#     NAELIST = 123
# func()
# print(NAELIST)
#输出结果为：['alex', 'eric']

#b.
# NAELIST = ['alex','eric']
# # def func():
# #     global NAELIST
# #     NAELIST = 123
# # func()
# # print(NAELIST)
#输出结果为：123

#c.
# NAMELIST = ['alex','eric']
# def func():
#     NAMELIST.append('seven')
# func()
# print(NAMELIST)
#输出结果为：['alex','eric','seven']

#d.
# NAMELIST = ['alex','eric']
# def func():
#     NAMELIST = 123
#     global NAMELIST
# func()
# print(NAMELIST)
#输出结果为：  *****报错******

#29.书写执行结果（禁止运行代码）
#a.
# name = 'root'
# def fun():
#     name = 'seven'
#     def outer():
#         name = 'eric'
#         def inner():
#             global name
#             name = '蒙逼了吧'
#         print(name)
#     print(name)
# print(name)
# ret = fun()
# print(ret)
# print(name)
#输出结果为：
# root
# seven
# None
# root


#b.
# name = 'root'
# def func():
#     name = 'seven'
#     def outer():
#         name = 'eric'
#         def inner():
#             global name
#             name = "蒙逼了吧"
#         print(name)
#     o = outer()
#     print(o)
#     print(name)
# ret = func()
# print(ret)
# print(name)
#输出结果为：
# eric
# None
# seven
# None
# root

#30.书写执行结果并解释每一步操作
#a.
# name = '苍老师'
# def outer(func):
#     name = 'alex'
#     func() #结果，就是执行的show
# def show():
#     print(name)
# outer(show)

#结果：'苍老师'


#b.
# name = '苍老师'
# def outer():
#     name = '波多'
#     def inner():
#         print(name)
#     return inner()
# ret = outer()
# print(ret)

#输出结果为：
# 波多
# None

#c.
# name = '苍老师'
# def outer():
#     name = '波多'
#     def inner():
#         print(name)
#     return inner
# ret = outer()
# ret()
# print(ret)
# result = ret()
# print(result)

#输出结果为：
# 波多
# <function outer.<locals>.inner at 0x0393A978>    #内存地址
# 波多
# None


#d.
# name = '苍老师'
# def outer():
#     name = '波多'
#     def inner():
#         print(name)
#     return inner  #返回内存地址
# ret = outer()
# print(ret)
# result = ret()  #执行inner函数，打印波多
# print(result)   #inner无返回值  打印的是None
#输出结果为：
# <function outer.<locals>.inner at 0x01BAA978>   #内存地址
# 波多
# None

#e.
# name = '苍老师'
# def outer(func):
#     def inner():
#         name = '李杰'
#         func()
#     return inner
# def show():
#     print(name)  #打印全局的
# outer(show)()
#输出结果为： '苍老师'


#31.书写执行结果并解释每一步操作
#a.
# def outer(func,z,y):
#     func(z)
# def show(x):
#     return  x*x
# ret = outer(show,9,23)
# print(ret)
#输出结果为：None

#b.
# def outer(func,z,y):
#    return func(z)
# def show(x):
#     return  x*x
# ret = outer(show,9,23)
# print(ret)
#输出结果为：81

#c.
# def outer(func,z,y):
#     func(z,y)
# f1 = lambda x,y:x + y
# ret = outer(f1,11,23)
# print(ret)
#输出结果为：None

#d.
# def outer(func,z,y):
#     return func(z,y)
# f1 = lambda x,y:x + y
# ret = outer(f1,11,23)
# print(ret)
#输出结果为：34


#32.写输出结果
# def f5(arg):
#     arg.append('偷到500万')
# def f4(arg):
#     arg.append('开第四个门')
#     f5(arg)
#     arg.append('关第四个门')
# def f3(arg):
#     arg.append('开第三个门')
#     f4(arg)
#     arg.append('关第三个门')
# def f2(arg):
#     arg.append('开第二个门')
#     f3(arg)
#     arg.append('关第二个门')
# def f1(arg):
#     arg.append('开第一个门')
#     f2(arg)
#     arg.append('关第一个门')
# user_list = []
# result = f1(user_list)
# print(user_list)
# print(result)
#输出结果：
# ['开第一个门', '开第二个门', '开第三个门', '开第四个门', '偷到500万', '关第四个门', '关第三个门', '关第二个门', '关第一个门']
# None


#b.
# def f5(arg):
#     arg = arg + 5
# def f4(arg):
#     arg = arg + 4
#     f5(arg)
#     arg = arg + 4
# def f3(arg):
#     arg = arg + 3
#     f4(arg)
#     arg = arg + 3
# def f2(arg):
#     arg = arg + 2
#     f3(arg)
#     arg = arg + 2
# def f1(arg):
#     arg = arg + 1
#     f2(arg)
#     arg = arg + 1
# num = 1
# result = f1(num)
# print(num)
# print(result)
#输出结果为：
# 1
#None

#c.
# def f5(arg):
#     arg = arg + 5
#     return arg
# def f4(arg):
#     arg = arg + 4
#     f5(arg)
#     arg = arg + 4
#     return arg
# def f3(arg):
#     arg = arg + 3
#     f4(arg)
#     arg = arg + 3
#     return arg
# def f2(arg):
#     arg = arg + 2
#     f3(arg)
#     arg = arg + 2
#     return arg
# def f1(arg):
#     arg = arg + 1
#     f2(arg)
#     arg = arg + 1
#     return arg
# num = 1
# result = f1(num)
# print(num)
# print(result)
#输出结果为：
# 1
# 3

#33.利用递归实现 1*2*3*4*5*6*7=5040
#第一种
# def func(x,y=1):
#     if x == 1:
#         return y
#     y = y * x
#     x -= 1
#     ret = func(x,y)
#     return ret
# ret = func(7)
# print(ret)

#第二种
# def func(x,y=1):
#     if x == 8 :
#         return y
#     y = y * x
#     x += 1
#     ret = func(x,y)
#     return ret
# ret = func(1)
# print(ret)

# reduce + lambda写法
# from functools import reduce
# print(reduce(lambda x,y:x*y,[x for x in range(1,8)]))

#34.写函数
#a.利用filter，自定义函数 获取l1中元素大于33的所有元素 l1=[11,22,33,44,55]

# l1 = [11,22,33,44,55]
# def f1(n):
#     return n > 33
# new_list =  filter(f1,l1)
# print(new_list)
# print(list(new_list))

#b.利用filter，lambda表达式 获取l1中元素小于33的所有元素 l1=[11,22,33,44,55]
# l1 = [11,22,33,44,55]
# new_list =  filter(lambda x:x<33,l1)
# print(list(new_list))


#c.利用map，自定义函数 将所有是奇数的元素加100  l1=[11,22,33,44,55]
# l1 = [11,22,33,44,55]
# def f2(n):
#     if  n %2 != 0:
#         n += 100
#         return n
#     else :
#         return n
# new_list = map(f2,l1)
# print(list(new_list))

#d.利用map ，lambda表达式 将所有是偶数的元素加 100 l1 = [11,22,33,44,55]
# l1 = [11,22,33,44,55]
# res=map(lambda i:i+100 if i%2==0 else i,l1)
# print(list(res))




#35.写程序
#a.文件操作时with的作用？
#with 打开文件执行完毕后自动关闭

#b.写程序利用with实现同时打开两个文件（一读，一写，并将读取的内容写入到写入模式的文件中）

# with open('a','r') as x,open('b','w') as y :
#     y.write(x.read())



#36.写函数：如有以下两个列表
#l1 = [...]
#l2 = []
#第一个列表的数字无序不重复排列，第二个列表为空列表
#需求：
#取出第一个列表的最小值放到第二个列表的首个位置
#取出第一个列表的最小值（仅大于上一次的最小值）放到第二个列表的首个位置
#取出第一个列表的最小值（仅大于上一次的最小值）放到第二个列表的首个位置,.......
#依次类推，从而获取一个有序的列表l2,并将其返回给函数调用者

# l1 = [1,5,4,6,8,3,2,9,0]
# l2 = []
# def func(la,lb):
#     if len(la) ==0:
#         return lb
#     lb.insert(0,la.pop(la.index(min(la))))
#     ret = func(la,lb)
#     return ret
# func(l1,l2)
# print(l2)


#37.猴子第一天摘下若干个桃子，当即吃了一半，还不过瘾就多吃了一个。第二天早上又将剩下的桃子吃了
#一半，还是不过瘾又多吃了一个。以后每天都吃前一天剩下的一半再加一个。到第10天刚好剩下一个。
#问猴子第一天摘了多少个桃子？1534

# taozi = 1
# day =  1
# while day < 10:
#     taozi = (taozi+1 )*2
#     day += 1
# print(taozi)







