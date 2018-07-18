#int 整形
#int  将字符串转换为数字
a ="123456"
#查看a的数据类型  用 type()
print(type(a))
b = int(a)
b += 1000
print(b)
#将字符串以整形输出 并以二进制输出
num = "01010101"
m =int(num,base=2)
print(m)

o = "a"
p = int(o,base=16)
print(p)

age = 10
r = age.bit_length()
print(r)
#age.bit_length() 就是整行转换二进制至少用几位来表示

