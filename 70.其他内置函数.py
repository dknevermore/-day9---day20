# print(chr(97))
# print(ord('a'))

# print(pow(2,3))  #2**3
# print(pow(2,3,5))    #2**3 取5的余

# 反转
l = [1,2,3,4]
print(list(reversed(l)))
print(l)

#四舍五入
print(round(3.5))

#转化成集合的形式
print(set('hello'))

#切片
# name = 'hello'
# s1 = slice(3,5)
# s2 = slice(1,4,2)
#print(name[3:5])
# print(name[s1])
# print(name[s2])
# print(s2.start)
# print(s2.stop)
# print(s2.step)

#排序

'''
l = [3,2,1,5,7]
l1 = [3,2,'a',5,7]
print(sorted(l))
#print(sorted(l1))   排序的本质就是在比较大小，不同类型之间不可以比较大小

people = [
     {'name': 'alex', 'age': 1000},
     {'name': 'wupei', 'age': 10000},
     {'name': 'yuanhao', 'age': 9000},
     {'name': 'RNG', 'age': 18}
]

print(sorted(people,key=lambda dic:dic['age']))

name_dic={
    'alex':200,
    'wupeiqi':300,
    'yuanhao':900
}
print(sorted(name_dic))
print(sorted(name_dic,key=lambda key:name_dic[key ]))
print(sorted(zip(name_dic.values(),name_dic.keys())))

'''

# print(str('1'))
# print(type(str({'a':1})))
# dic_str= str({'a':1})
# print(type(eval(dic_str)))


'''
#求和
l = [1,2,3,4]
print(sum(l))
print(sum(range(5)))


#查看数据类型
print(type(l))

msg = '123'
if type(msg) is str:
    msg = int(msg)
    res = msg+1
    print(res)


def test():
    msg= '哈哈哈哈啊哈'
    print(locals())
    print(vars())
test()
print(vars(int))

'''
#模块就是py文件
#import------>sys------->__import__()

#import test  #不能导入字符串 模块名
#test.say_hi()

module_name='71test'
m =__import__(module_name)  #__import__()可以导入字符串模块名
m.say_hi()
