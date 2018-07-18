#字典
#dict
#1.字典的基本结构
'''
info = {
    "k1": "v1", #键值对
    "k2": "v2"
}
'''
# 2.字典的value可以是任何值
# 3.布尔值（0，1）可能会重复，列表，字典不能作为字典的key
# 4.字典无序
# 5.字典支持del 删除的
info = {
    "k1": 18,
     2: True,
    "k3": [
        11,
        [],
        (),
        22,
        33,
        {
            "kk1":'vv1',
            "kk2":'vv2',
            "kk3":(11,22),
        },
            ],
    "k4":(11,22,33,44),
}
#6.索引方式找到指定元素
v = info["k1"]
print(v)
v1 = info[2]
print(v1)
v2 = info["k3"][5]['kk3'][0]
print(v2)
# 5.1.删除
del info["k1"]
print(info)
# 7.字典for循环默认循环输出它key
for item in info :
    print(item)
for item1 in info.keys() :
    print(item1)
for item2 in info.values():
    print(item2)

for k,v in info.items():
    print(k,v)

