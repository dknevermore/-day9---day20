# in   与  not in             不等于 !=   <>      等于  ==
# 结果：布尔值                 大于等于 >=       小于等于  <=
name = "哈哈哈"
v = "哈" in name
print(v)

if v :
    print("66666666666")
else :
    print("888888888888888")
t = 1==1
print(t)
#测试  and  的 用法  一假即都假
if 1==1 and 2==2 :
    print("真")
else :
    print("假")
#测试   or 的 用法   一真即都真
if 1==1 or 2==3 :
    print("真")
else :
    print("假")
#补充：  如果多个判断的时候，先判断括号里面的
if  1==1 and (2==2 or 3==3) :
    print("真")
else :
    print("假")
#补充   如果没有括号的话，先判断第一个然后 与 and 或 or 比较
#例如: 如果第一个and 前面是真 那么还要继续判断后面 ，如果第一个and前面是假  那么就不用再判断了，因为这整个值都是假的
#or 同理
if 1==1 and  2==2  or  3==3   and  4==4 :
    print("真")
else :
    print("假")


