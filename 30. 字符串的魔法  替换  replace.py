#注意********
#字符串一旦创建， 就不可修改
#一旦修改或者拼接，都会造成重新生成字符串
#替换
test = "alexalexalexalex"
v = test.replace("ex",'bbb')
print(v)
#只替换前一个字符
v1 = test.replace("ex",'bbb',1)
print(v1)
v2 = test.replace("ex",'bbb',2)
print(v2)
