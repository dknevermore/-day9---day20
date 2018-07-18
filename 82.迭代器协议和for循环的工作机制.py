#迭代器协议
#1.迭代器协议是指：对象必须提供一个next方法，执行该方法要么返回迭代器中的下一项，要么就引起一个
#Stoplteration异常，以终止迭代（只能往后走不能往前退）

#2.可迭代对象：实现了迭代器协议的对象（如何实现：对象内部定义一个__iter__()方法）

#3.协议是一种约定，可迭代对象实现了迭代器协议，python的内部工具（如for循环，sum，min，max函数等）使用迭代器协议访问对象。

#for循环的本质：循环所有对象，全都是使用迭代器协议

#(字符串，列表，元组，字典，集合，文件对象)这些都不是可迭代对象，只不过在for循环式，调用了他们内部的__iter__方法，把他们变成了可迭代对象

#然后for循环调用可迭代对象的__next__方法取值，而且for循环会捕捉Stoplteration异常，以终止迭代


x = 'hello'
iter_test=x.__iter__()

print(iter_test)
print(iter_test.__next__())
print(iter_test.__next__())
print(iter_test.__next__())
print(iter_test.__next__())
print(iter_test.__next__())


l = [1,2,3]
for i in l :  #i_l=l.__iter__()  i_l.__next__()
    print(i)

l2 = [6666666666666666,999999999999,5,6,78,89,9]
iter__l2  = l2.__iter__() #遵循迭代器协议，生成可迭代对象
print(iter__l2.__next__())
print(iter__l2.__next__())


l3 = [77777,88888,99999,101010101]
m = l3.__len__()
print(m)
print(len(l3))
index = 0
while index < m :
    print(l3[index])
    index += 1


s = {66666,99999,11111111}
iter_s = s.__iter__()
print(iter_s)
print(iter_s.__next__())
print(iter_s.__next__())
print(iter_s.__next__())


dic = {'a':1,'b':2}
iter_d=dic.__iter__()
print(iter_d.__next__())  #key的值

#****************for循环的实质*************
l4= [1,2,3,4,5,6]
diedai_l = l4.__iter__()
while True :
    try:
        print(diedai_l.__next__())
    except StopIteration :
        print('迭代完毕了，循环终止了')
        break