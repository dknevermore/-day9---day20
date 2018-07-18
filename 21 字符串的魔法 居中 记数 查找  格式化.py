# str   可以按住ctrl 点 str 进入str 的源代码  进而查看功能

#首字母大写
test = "alex"
v = test.capitalize()
print(v)

#都变小写
# test.casefold()  牛逼一点
# test.lower()

#设置宽度并将内容居中
#20代指总长度
# * 代指空白位置填充 只能填一个字符 可有可无
v1 = test.center(20)
v2 = test.center(20,"*")
print(v1)
print(v2)

#数一下该字符在字符串里面出现过多少次
#后面的参数代表起始位置和结束位置
v3 = test.count('a')
print(v3)
pi = "aeaeaeaeae"
v4 = pi.count('a',3,8)
print(v4)

#encode 和 decode  之后再讲 这个非常重要

#以  该字符 为结尾 / 开头 来判断真假  这也可以像上面一样在后面加参数来选择位置判断
v5 = test.endswith('x')
v6 = test.startswith('a')
print(v5)
print(v6)

#从开始往后找，找到第一个之后，获取其位置  如果未找到 返回 -1这个值

#后面加的参数  >= 和 <
po = "alexalex"
v7 = po.find('ex',5,8)
print(v7)

#格式化，将一个字符串中的占位符替换为指定的值
kk = "i am {name}, age {a}"
print(kk)
v8 = kk.format(name='alex',a=19)
print(v8)


#按顺序填入
pp = "i am {0}, age {1}"
print(pp)
v9 = pp.format('alex',19)
print(v9)



#格式化 的 {"name":'alex',"a":19}
kk = "i am {name}, age {a}"
print(kk)
v10 = kk.format_map({"name":'alex',"a":19})
print(v10)

#与find类似  但是如果找不到的话就会报错  最好用find
qq = "alexalex"
v11 = qq.index('ex')
print(v11)

#字符串中是否只包含字母和数字两者或两者之一
cc = "kasfk21654"
v12 = cc.isalnum()
print(v12)
# cc.isdigit() 只包含数字
# cc.isalpha() 只包含字母
