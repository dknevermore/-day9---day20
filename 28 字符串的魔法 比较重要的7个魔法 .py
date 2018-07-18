#7个比较重要的魔法
#插入①
test = "  djhakjashad1a21   "
v = "   ".join(test)
print(v)
#分割②
v2 = test.split('a',3)
print(v2)
#查找③
v3 = test.find('a')
print(v3)
#去除左右空格④
v4 = test.strip()
print(v4)
#upper 大写⑤
#lower  小写⑥

#替换⑦
test = "alexalexalexalex"
v = test.replace("ex",'bbb')
print(v)
#只替换前一个字符
v1 = test.replace("ex",'bbb',1)
print(v1)
v2 = test.replace("ex",'bbb',2)
print(v2)


