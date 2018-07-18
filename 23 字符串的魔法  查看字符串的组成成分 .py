#查看是否只有字母，汉子组成
test = "hahah哈haha"
v = test.isalpha()
print(v)

#查看当前输入是否只有数字组成 后者更牛b一点 可输入  二  ②  来看它们三的区别
#有小数点都是False     用的最多的还是isdecimal
shu ="123456789"
v1 = shu.isdecimal()
v2 = shu.isdigit()
v5 = shu.isnumeric()
print(v1,v2,v5)

#字母 数字 下划线 标识符 isidentifier class
a = "ssadsaadjadasdkjf_kjk4111"
v3 = a.isidentifier()
print(v3)

#判断是否都是小写  islower()    lower()把它变成小写
#lower()把它变成小写   用于网站验证大小写即可  就是把字符串统一变成小写再比较
v4 = a.islower()
print(v4)

pi = "GGGGGGGGGG"
z = pi.lower()
print(z)
#判定字符串是否是大写  和 把字符串全部转换成大写
x = pi.isupper()
print(x)
c = a.upper()
print(c)

#是否存在不可显示的字符
#\t  制表符
#\n  换行
da = "jdsfhjsdajkfaslkj"
v6 = da.isprintable()
print(v6)

#判断是否全部是空格
ko = "    "
v7 = ko.isspace()
print(v7)

#把字符串全部变成文章的标题
ka = "Return TRUE if all cased characters is  are uppercase and there is"
v8 = ka.title()
print(v8)

#判断字符串是否为标题 即每个首字母都是大写
ki = "Return TRUE if all cased characters is  are uppercase and there is"
v9 = ki.istitle()
print(v9)