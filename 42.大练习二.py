#8.转换
#a.将字符串 s = "alex" 转换成列表
#b.将字符串 s = "alex" 转换成元组
#c.将列表  li =["alex","seven"] 转换成元组
#d.将元组 tu =('Alex',"seven") 转换成列表
'''
s = "alex"
li =["alex","seven"]
tu =('Alex',"seven")
new_li = list(s)
print(new_li)

new_tu = tuple(s)
print(new_tu)

new_tu1 = tuple(li)
print(new_tu1)

new_li1 = list(tu)
print(new_li1)
'''
#9.元素分类
#有如下值集合[11,22,33,44,55,66,77,88,99,90],将所有大于 66 的值保存至字典的第一个key中，
#将小于 66 的值保存的第二个key中
#即：{"k1":大于66的所有值,,"k2"小于66的所有值}
"""
li = [11,22,33,44,55,66,77,88,99,90]
dic = {}
li1 = []
li2 = []
for item in li :
    if item > 66 :
        li1.append(item)
        dic = {"k1" : li1,"k2" : li2}
    elif item < 66 :
        li2.append(item)
        dic = {"k1" :li1 ,"k2" : li2}
    else: pass
print(dic)
"""

#10.输出商品列表，用户输入序号，显示用户选中的商品
#商品 li = ['手机','电脑','鼠标垫','游艇']
#a.允许用户添加商品
#b.用户输入序号显示内容
'''
dic = {}
k = 0
li = ['手机','电脑','鼠标垫','游艇']
for item in li :
    k = int(li.index(item))
    dic.setdefault(k,item)
print(dic)
v2 = int(input("序号:"))
v3 = str(input("商品名:"))
dic.setdefault(v2,v3)
print(dic)
#v1 = input("请输入序号")
while 0==0 :
    v = dic.get(int(input("请输入序号")))
    print(v)

'''

#12.列举布尔值是False的所有值
# 0  None []  ()  {} ==> False

#13.有两个列表
#l1 = [11,22,33]
#l2 = [22,33,44]
#a.获取内容相同的元素列表
#b.获取l1中有，l2中没有的元素列表
#c.获取l2中有，l1中没有的元素列表
#d.获取 l1和l2 中内容都不同的元素
'''
l1 = [11,22,33]
l2 = [22,33,44]
for item in l1 :
    if item not in l2 :
        print(item)
    else:
        pass
for item in l2:
    if item not in l1:
        print(item)
    else:
        pass

'''

#14.利用For循环和range输出
#a.For循环从大到小输出 100-1
#b.For循环从小到大输出 1-100
#c.While循环从大到小输出 100-1
#d.While循环从小到大输出 1-100
'''
v = range(100,0,-1)
for q in v :
    print(q)
v1 = range(1,101,1)
for w in v1 :
    print(w)

n = 100
while n > 0 :
    print(n)
    n -= 1

n1 = 1
while n1 < 101 :
    print(n1)
    n1 += 1
'''

#15.购物车
#功能要求：
#    要求用户输入总资产，例如：2000
#    显示商品列表，让用户根据序号选择商品，加入购物车
#    购买，如果商品总额大于总资产，提示账户余额不足，否则，购买成功
'''
goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
        ]
money = 2000
dic = {}
k = 0
for item in goods :
    k = int(goods.index(item))
    dic.setdefault(k,item)

for item1 in dic :
    print(item1,dic.get(item1))

li = []
while True :
    x = int(input("请输入购买序号："))
    li.extend([x])
    print("购买的序号为：",li)
    if input("是否继续选择(y=是)其他任意键退出 ") == "y":
        pass
    else:
        break
s = 0
for kk in li :
    s +=((dic.get(kk)).get('price'))

if s < 2000 :
    print("购买成功","金额为：",s)
else:
    print("余额不足")

'''

#16.分页显示内容
#   a.通过for循环创建301条数据，数据类型不限，如:
#       alex-1      alex1@live.com   pwd1
#       alex-2      alex2@live.com   pwd2
#       alex-3      alex3@live.com   pwd3
#       ...

#   b.提示用户 请输入要查看的页码，当用户输入指定页码，则显示指定数据

#   注意:
#   - 每页显示10条数据
#   - 用户输入页码是非十进制数字，则提示输入内容格式错误
'''
li = []
for i in range(1,302,1) :
    s1 = [{"name":"alex"+str(i),"email":"alex1@live.com","pwd":str(i)}]
    li.append(s1)
dic = {}
n = 10
v =li[0:10]
while n < 302 :
    dic.setdefault(n/10,li[n-10:n])
    n += 10
i = int(input("请输入页码"))
if i not in range(0,31) :
    print("输入内容格式错误")
else:
    c = dic.get(i,0)
    for pp in c :
        print(pp)

'''

#17.有1、2、3、4、5、6、7、8 8个数字，能组成多少个互不相同且无重复数字的两位数？
'''
c = 0
for i in range(1, 9):
    for v in range(1, 9):
        if i != v :
            c += 1
        else:
            pass
print(c)
'''


#18.利用for循环和range输出 9*9乘法表
'''
for i in range(1,10):
    st = ""
    for v in range(1,i+1):
        st +=str(i)+"*"+str(v)+"="+str(i*v)+"\t"
    print(st)
'''



#19.有以下列表
#nums = [2,7,11,15,1,8,7]
#请找到列表中任意两个元素相加能够等于9的元素集合，如：[(0,1)(4,5)]
'''
nums = [2,7,11,15,1,8,7]
li = []
for i in  nums :
    for v in nums :
        if i + v == 9 :
            li.append((v,i))
        else :
            pass
print(li)

'''
#20.用python开发程序自动计算方案
#       公鸡5文钱一只，母鸡3文钱一只，小鸡3只一文钱，用100文钱买100只鸡，其中公鸡，母鸡，小鸡都必须要有，
#       问公鸡，母鸡，小鸡要买多少只刚好凑足100文钱？
'''
for x in range(1,100//5):
    for y in range(1,100//3):
        for z in range(1,301):
            if x + y + z == 100 and 5*x + 3*y + z/3 == 100 :
                print(x,y,z)
'''
