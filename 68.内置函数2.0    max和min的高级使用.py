# l = [1,3,100,-1,2]
# print(max(l))       #最大值
# print(min(l))       #最小值



# people = [
#     {'name': 'alex', 'age': 1000},
#     {'name': 'wupei', 'age': 10000},
#     {'name': 'yuanhao', 'age': 9000},
#     {'name': 'RNG', 'age': 18}
# ]

age_dic = {'alex_age':18,'wupeiqi_age':20,'zsc_age':100,'lhf_age':30}
print(max(age_dic.values()))

#默认比较字典的key
#print(max(age_dic))

for item in zip(age_dic.values(),age_dic.keys()):#(18,'alex_age') (20,'wupeiqi_age') () () ()
    print(item)

print(list(max(zip(age_dic.values(),age_dic.keys()))))


l =[
    (5,'e'),
    (1,'b'),
    (3,'a'),
    (4,'d')
]
#l1 = ['a10','b12','c10'，100] #不同类型之间不能进行比较
l1 = ['a10','a2','c10']
print(list(max(l)))
print(list(max(l1)))