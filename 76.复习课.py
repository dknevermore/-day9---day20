#map
# l = [1,2,3,4,5]
# res1 = list(map(str,l))
# res = list(map(lambda x:str(x),l))
# print(res1)
# print(res)

#reduce
# from functools import reduce
# l = [1,2,3,4,5]
# #reduce(func,l)
# res2 = reduce(lambda x,y:x+y,l,3)
# print(res2)

#filter
# name = ['alex_sb','linghaifneg']
# res3 = filter(lambda x:not x.endswith('sb'),name)
# print(list(res3))


#w文件操作
# f = open('test11.py','w',encoding='utf-8')   #文件以什么编码存的就以什么编码打开
# f.write('1111111\n')
# f.write('1111111\n')
# f.write('1111111\n')
# f.write('1111111\n')
# f.close()

# f = open('test11.py','a',encoding='utf-8')
# f.write('这是a模式的内容')
# f.close()

# f = open('tset11.py','r+',encoding='utf-8')
# f.write('hello')

