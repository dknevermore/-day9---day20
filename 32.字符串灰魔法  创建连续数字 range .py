#for 循环中break  和 continue 也是适用的
test = "我好帅啊啊啊啊啊"
for item in test :
    print(item)

#帮助创建连续的数字,通过设置步长来指定不连续
#范围 0=<   < 100
v = range(0,100,5)
print(v)
v1 = range(100,0,-1)
print(v1)
for kk in v :
    print(kk)
for qq in v1 :
    print(qq)

