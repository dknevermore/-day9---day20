#绝对值
print(abs(-1))
print(abs(1))

#列表判断   返回布尔值  一假全假 ，但空列表，空字符串为真
print(all([1,2,'1']))
print(all([1,2,'1','']))
print(all([1,2,'1',0]))
print(all(''))


#列表判断   返回布尔值  一真全真
print(any([0,'']))
print(any([0,'',1]))


#把十进制转成二进制   0b开头就代表二进制
print(bin(86))


#空，None，0的布尔值为False，其余都为True
print(bool(''))
print(bool(None))
print(bool(0))

#字节
name = "你好"
print(bytes(name,encoding='utf-8'))  #编码转换二进制
print(bytes(name,encoding='utf-8').decode('utf-8'))  #解码  默认的就是'utf-8'
print(bytes(name,encoding='gbk'))    #编码转换二进制
print(bytes(name,encoding='gbk').decode('gbk'))  #解码
#print(bytes(name,encoding='ascii'))   # ascii不能编码中文

#按照ascii表打印对应的字符
print(chr(97))

#查看某一个对象都有哪些方法,   光打印方法的名字
print(dir(dict))

#取商得余数   #网站中的分页
print(divmod(10,3))

#eval()把字符串中的数据结构给提取出来-
dic= {'name':'alex'}
dic_str=str(dic)
print(dic_str  )
d1 = eval(dic_str)     #eval()把字符串中的数据结构给提取出来-
print(d1["name"])

#把字符串中的表达式进行运算
express='1+2*(3/3-1)-2'
print(eval(express))

#可hash的数据类型即不可变数据类型，反之,不可hash的数据类型即可变数据类型
#可查看对象是否被修改了
print(hash('216hknnfkjj542plksjajdp165421'))
print(hash('216hknnfkjj5dkjaskdjlakj42165421'))
name1='alex'
print(hash(name1))
print("---> before",hash(name1))
name1='sb'
print("---> after",hash(name1))


#查看方法的解释
print(help(all))

print(bin(10))  #10进制--> 2进制
print(oct(12))  #10进制--> 8进制
print(hex(12))  #10进制--> 16进制


#打印对象的内存地址
print(id("1234565"))

#判断或查看对象类型
print(isinstance(1,int))
print(isinstance('dksaj',int))
print(isinstance('dksaj',str))
print(isinstance(["sdaj,2,3,3"],list))
print(isinstance(["sdaj,2,3,3"],dict))
print(isinstance({},dict))
print(isinstance({1,2,3},set))


name10 = "哈哈哈哈哈哈哈啊哈"
print(globals())  #查看全局变量名
print(__file__)   #查看文件名


def test():
    age="111111111111111111111"
    #print(globals())
    print(locals())    #查看局部变量名
test()


l = [1,3,100,-1,2]
print(max(l))       #最大值
print(min(l))       #最小值

print(list(zip(('a','b','c'),(1,2,3))))
print(list(zip(('a','b','c'),(1,2,3,4))))
print(list(zip(('a','b','c','d'),(1,2,3))))

#拉链方法
p = {'name':'alex','age':18,'gender':'none'}
print(zip(p.keys(),p.values()))
print(list(zip(p.keys(),p.values())))
print(list(zip(['a','b'],'123465')))