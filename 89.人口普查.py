def get_polution():
    with open('89.人口普查.txt','r',encoding='utf-8') as f :
        for i in f :
            yield i

g = get_polution()
#print(g.__next__()['population'])   会报错
# s1 = eval(g.__next__())    #转换为字典的函数  eval()
# print(type(s1))
# print(s1['population'])

'''
res = 0
for p in g:
    p_dic = eval(p)
    print(p_dic['population'])
    res += p_dic['population']
print(res)

'''
all_popu = sum(eval(i)['population'] for i in g)
print(all_popu)

# for p in g :                #不执行因为 g 都迭代完了
#     print(eval(p)['population']/all_popu)
