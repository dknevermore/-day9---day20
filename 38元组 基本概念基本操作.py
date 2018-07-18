# 元组, 元素一级不可被修改，不能被增加或者删除
#tu.count(33) 获取指定元素在元组中出现的次数
#tu.index(22) 根据值获取当前值索引位置（左边优先）
# tuple
#1.书写格式
tu = (111,"alex",(11,22,),[(33,44)],True,33,44, )
#一般写元组的时候，推荐在最后加入 ，
#2.索引
v = tu[0]
print(v)
#3.切片
v1 = tu[0:2]
print(v1)
#4.可以被for循环，可迭代对象
for item in tu :
    print(item)

# 5.转换
s = "dksalkdsakj54"
li = ["skajd",32555]
tu1 = (2123,744,"asdk")
tu00 = ("sdja","jksajd","aksdj")

v2 = tuple(s)
print(v2)
v3 = tuple(li)
print(v3)
v3 = list(tu1)
print(v3)
q = " ".join(tu00)
print(q)
li.extend((11,22,33, ))
print(li)


#6.元组的一级元素不可修改/删除/增加
tu2 = (111,"alex",(11,22,),[(33,44)],True,33,44, )
#元组是有序的
v4 = tu2[3][0][0]
print(v4)
v5 = tu2[3][0] = 564
print(tu2)


