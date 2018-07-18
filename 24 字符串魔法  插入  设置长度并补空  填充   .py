#*********将字符串的每一个元素按照指定分隔符进行拼接  非常非常重要
test = "你是风儿我是沙"
print(test)
t = '   '
v = t.join(test)
print(v)

#设置长度，然后指定字符填充空白位置
zuo = "alex"
z = zuo.ljust(20,"*")
print(z)

you = "saitama"
r = you.rjust(20,"*")
print(r)

# 也是同上的功能，但只能用零填充 所以基本不用
lin = "mofashi"
j = lin.zfill(20)
print(j)



