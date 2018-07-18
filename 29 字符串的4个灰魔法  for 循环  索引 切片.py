########### 灰魔法 ###########
#len() for循环 索引 切片  在其他数据类几乎都能用
test = "alex"
#索引，下标，获取字符串中的某一个字符
h = test[0]
print(h)

#切片
#索引范围   0=<   <1
h1 = test[0:1]
print(h1)

#获取当前字符串中有几个字符组成
h2 = len(test)
print(h2)

#len 和 join 括号里除可以加字符串  还可以加入 列表
lie = [111,222,545456,548,8,18,18,1,855,18,]
h3 = len(lie)
print(h3)
#插入
h4 = "  ".join("oskajdojsaod")
print(h4)

wen = "人生于世上有多少知己"
index = 0
while index < len(wen) :
    v  = wen[index]
    print(v)
    index += 1

#for 循环
# for 变量名 in 字符串:
#     变量名
for zzz in wen :
    print(zzz )




