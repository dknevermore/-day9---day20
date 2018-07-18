#1.max函数处理的是可迭代对象，相当于一个for循环取出每个元素进行比较
#注意。不同类型之间不能不较
#2.每个元素间进行比较，是从每个元素的第一个位置一次比较，如果这一位置
#分出大小，后面的都不需要比较了，直接得出这俩元素的大小

l = [1,3,100,-1,2]
print(max(l))
dic={'age':18,'age2':10}
print(max(dic))  #比较的是key
print(max(dic.values())) #比较的是values ，但是不知道是那个key对应的
print(max(zip(dic.values(),dic.keys())))  #结合zip使用

people = [
     {'name': 'alex', 'age': 1000},
     {'name': 'wupei', 'age': 10000},
     {'name': 'yuanhao', 'age': 9000},
     {'name': 'RNG', 'age': 18}
]

print('---->',max(people,key=lambda dic:dic['age']))
ret = []
for item in people:
    ret.append(item['age'])
print(ret)
print(max(ret))