# 1、执行 Python 脚本的两种方式
#  命令行模式 python  开始写
#  命令行模式 python  路径文件名.py

# 2、简述位、字节的关系
#   8位（bit）=1字节（Byte）,1024字节=1KB；
# 3、简述 ascii、unicode、utf-­‐8、gbk 的关系
#先出现的顺序ascii
#           unicode
#           utf-­‐8
#           gbk

# 4、请写出 “李杰” 分别用 utf-­‐8 和 gbk 编码所占的位数
# 一个字节 8位
#            48位      和  32位     utf-­‐8 一个汉字3个字节
#                                     gbk      一个汉字2个字节
# len() 在 python 3  字符
#          python 2  字节
# 5、Pyhton 单行注释和多行注释分别用什么？
#  单行注释：#
#  多行注释："""
#
#            """
#   三个单引号也可以

# 6、声明变量注意事项有那些？
#数字，字母，下划线
#变量名不能和关键字重复 也不能和python内置的关键字重复
#虽然不会报错但是 原本的关键字的功能就不能用了

# 7、如有一下变量 n1 = 5，请使用 int 的提供的方法，得到该变量最少可以用多少个二进制位表示？
laa = 5
laaq = laa.bit_length()
print(laaq)
#    三位二进制  101

# 8、布尔值分别有什么？ 补充  bool(a)
#  True  False
# 空字符串：""==>  假    |  只要有字符 "daswca"==>真

# 9、阅读代码，请写出执行结果
# a = "alex"
# b = a .capitalize()
# print(a)
# print(b)
#
# 请写出输出结果： alex    和    Alex
#
# 10、写代码，有如下变量，请按照要求实现每个功能
name = " aleX"
# a. 移除 name 变量对应的值两边的空格，并输入移除后的内容
a = name.strip()
print(a)

# b. 判断 name 变量对应的值是否以 "al" 开头，并输出结果
b = name.startswith('al')
print(b)

# c. 判断 name 变量对应的值是否以 "X" 结尾，并输出结果
c = name.endswith('X')
print(c)

# d. 将 name 变量对应的值中的 “l” 替换为 “p”，并输出结果 e. 将 name 变量对应的值根据 “l” 分割，并输出结果。
e = name.replace('l','p')
print(e)
d = name.split('l')
print(d)

# f. 请问，上一题 e 分割之后得到值是什么类型（可选）？
#  列表

# g. 将 name 变量对应的值变大写，并输出结果
g = name.upper()
print(g)

# h. 将 name 变量对应的值变小写，并输出结果
h = name.lower()
print(h)

# i. 请输出 name 变量对应的值的第 2 个字符？
i = name[1]
print(i)

# j. 请输出 name 变量对应的值的前 3 个字符？
j = name[0:3]
print(j)

# k. 请输出 name 变量对应的值的后 2 个字符？*********
k = name[-2:]
print(k)

# l. 请输出 name 变量对应的值中 “e” 所在索引位置？
l = name.find('e')
print(l)
# m. 获取子序列，仅不包含最后一个字符。如： oldboy 则获取 oldbo; root 则获取 roo
v = len(name)
q = len(name) -1
print(name[0:q])

# 21、字符串是否可迭代对象？如可以请使用 for 循环每一个元素？
#只要能被for循环的就是可迭代对象
kasa =" 我RNG天下无敌"
for sa in kasa :
    print(sa)

# 22、请用代码实现：
# a. 利用下划线将列表的每一个元素拼接成字符串，
li = "alexericrain"
a1 = "_".join(li)
print(a1)

# b. 利用下划线将列表的每一个元素拼接成字符串，
li2 = ['alex', 'eric', 'rain']
b1 = "_".join(li2)
print(b1)

# 23、Python2 中的 range 和 Python3 中的 range 的区别？
# Python2中range会输出range的每个值   立即创建
# Python3 中range只会表示区间的形式    只有在迭代循环中才 创建

# 24、实现一个整数加法计算器：
#content = input('请输入内容：')	 如： 5+9 或 5+ 9 或 5 + 9
value = input("请输入加法")
v1,v2 = value.split('+')
yu = int(v1) + int(v2)
print("等于",yu)

# 25、计算用户输入的内容中有几个十进制小数？几个字母
# 如：
#content = input('请输入内容：') # 如：asduiaf878123jkjsfd-­‐213928
cc = input("请输入内容：")
n = 0
m = 0
for ee in cc :
    s = ee.isdigit()
    if s == True :
        n += 1
    else:
        pass
    z = ee.isalpha()
    if z == True :
        m += 1
    else :
        pass
print("数字：",n,"字母：",m)

# 26、简述 int 和 9 等数字 以及 str 和 "xxoo" 等字符串的关系？
#   int str  都是类 或 类型
#   9 和 "xxoo" 都是根据类或类型创造的 对象


# 27、制作趣味模板程序需求：等待用户输入名字、地点、爱好，根据用户的名字和爱好进行任意现实
# 格式化
dui = "帅哥是 {0} ,喜欢 {1}"
name1 = input("名字：")
like = input("事：")
jj = dui.format(name1,like)
print(jj)

# 28、制作随机验证码，不区分大小写。流程：
#
# -­‐ 用户执行程序 -­‐
#      给用户显示需要输入的验证码 -­‐
#      用户输入的值
#
# 用户输入的值和显示的值相同时现实正确信息；否则继续生成随机验证码继续等待用户输入生成随机验证码代码示例：




# 29、开发敏感词语过滤程序，提示用户输入内容，如果用户输入的内容中包含特殊的字符：如 "苍老师" "东京热"，则将内容替换为 ***
k = input("请写点什么：")
l = len(k)
k1 = k.replace("苍井空","****",l)
print(k1)
#
#
# 30、制作表格循环提示用户输入：用户名、密码、邮箱 （要求用户输入的长度不超过 20 个字符，如果超过则只有前 20 个字符有效）
# 如果用户输入 q 或 Q 表示不再继续输入，将用户输入的内容以表格形式打印
s = ""
while True :
    yong = input("用户名：")
    mima = input("密码：")
    youx = input("邮箱：")
    g = "{0}\t{1}\t{2}\n"
    g1 = g.format(yong[0:20],mima,youx)
    s += g1
    if yong == "q"or mima == "q" or youx == "q":
        break
    else :
        continue
print(s.expandtabs(20))











