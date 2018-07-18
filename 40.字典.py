#字典
#dict
dic = {
    "k1": 'v1',
    "k2": 'v2',
    "k3": 'v3',
    "k4": 'v4',
    "k5": 'v5'
}
#1.根据序列，创建字典，并指定统一的值
v = dict.fromkeys(["k1",123,"999"],123)
print(v)
#2.根据key获取值，key不存在时,可以指定默认值（None）
v1 = dic.get('k1',None)
print(v1)
v2 = dic.get('k111111',None)
print(v2)
#3删除并获取
v3 = dic.pop("k1")
print(dic,v3)
k,v4 = dic.popitem()
print(dic,k,v4)

#4.设置值
# 已存在，不设置，获取当前key对应的值
# 不存在，设置，获取当前key对应的值
v5 = dic.setdefault("k1",'123')
print(dic,v5)
v6 = dic.setdefault("k1111",'123123456')
print(dic,v6)

#5.更新
dic1 = {
    "k10": 'v10',
    "k11": 'v11'
    }
dic1.update({'k10':'11111111111','k13':123})
# print(dic1)
#dic1.update(k10=123,k3=8545,k5="asdas")
print(dic1)

#6.keys()   7.values()   8.items()  get  update


