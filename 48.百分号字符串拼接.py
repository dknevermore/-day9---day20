msg = 'i am %s my hobby is %s' %('rng','alex')  #  %s 可以接收一切
print(msg)

ms = 'i am %s my hobby is %s' %('rng',1)
print(ms)

mg = 'i am %s my hobby is %s' %('rng',[1,2,3,4,5,6])
print(mg)

ggg = 'i am %s my hobby is %d' %('rng',666)  #  %d 只能接收数字
print(ggg)

hhh = "percent %.2f" % 99.976236666    # 打印浮点数%f
print(hhh)                               # %.2f表示保留小数后两位


bbb = "percent %.2f %%" % 99.976236666   # %% 打印百分号
print(bbb)

ddd = "percent %.3s" % "ssssssssssss"     #打印字符串的前两位截取
print(ddd)

tp1 = "i am %(name)s age %(age)d " % {"name":"alex","age":18}
print(tp1)             #通过  key   字典
tp2 = "percent %(pp).2f %%" % {"pp":99.5545454123}
print(tp2)

jjj = 'i am %(name)-60s my hobby is alex' %{'name':'RNG'}
print(jjj)             #左对齐设置空白
uu = 'i am %(name)+60s my hobby is alex' %{'name':'RNG'}
print(uu)              #右对齐设置空白

yyy = 'i am \033[45;1m%(name)+60s\033[0m my hobby is alex' %{'name':'RNG'}
print(yyy)            #加颜色   \033[45;1m .....\033[0m

