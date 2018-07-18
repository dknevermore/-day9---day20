#分隔符  但有所区别
test = "testdkfsajlk"
v = test.partition('s')
print(v)
v1 = test.rpartition('s')
print(v1)
#test.split('s',1)后面是可以加参数的
v2 = test.split('s')
print(v2)
v3 = test.rsplit('s')
print(v3)
#以后会学正则表达式