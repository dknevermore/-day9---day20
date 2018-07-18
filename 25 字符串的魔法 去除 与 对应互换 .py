#默认去除左右空白  \t  \n
test = " alex "
v = test.lstrip()
print(v)
v2 = test.rstrip()
print(v2)
v3 = test.strip()
print(v3)
#也可指定字符匹配去除 指定字符会多重拆分匹配去除
#优先最多匹配
pi = "123456789"
v4 = pi.lstrip('1325')
print(v4)

#设置对应关系，之后对应互换
ni = "aeiou"
po = "12345"
m = str.maketrans("aeiou","12345")
t = "aioueaoiushfdfsdnia"
v5 = t.translate(m)
print(v5)