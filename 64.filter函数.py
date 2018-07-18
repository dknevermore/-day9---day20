'''
movie_people = ['sb_1hao','rng','sb_2hao']

def filter_test(array):
    ret = []
    for p in array:
        if not p.startswith('sb'):
            ret.append(p)
    return ret
res = filter_test(movie_people)
print(res)

'''
#
# movie_people = ['1hao_sb','rng','sb_2hao_sb']
#
# def show_sb(n):
#     return n.endswith('sb')
#
# def filter_test(func,array):
#     ret = []
#     for p in array:
#         if not func(p):
#             ret.append(p)
#     return ret
# res = filter_test(show_sb,movie_people)
# print(res)

#终极版本+
movie_people = ['1hao_sb','rng','2hao_sb']

#def show_sb(n):
#     return n.endswith('sb')
#lambda n:n.endswith('sb')

def filter_test(func,array):
     ret = []
     for p in array:
         if not func(p):
             ret.append(p)
     return ret
res = filter_test(lambda n:n.endswith('sb'),movie_people)
print(res)
#***********************filter函数*******************************
res1 = filter(lambda n:not n.endswith('sb'),movie_people)
print(res1)
res2 = list(filter(lambda n:not n.endswith('sb'),movie_people))  #函数处理的结果是布尔值，如果布尔值等于True  这个值要保留下来
print(res2)      #方法(lambda n:not n.endswith('sb))处理后面的可迭代对象(movie_people)  for循环依次把元素赋值给方法 之后有判断
                 #filter得到的结果也是可迭代对象



