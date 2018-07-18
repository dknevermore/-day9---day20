##########################深灰魔法########################
#列表   list   类
#1. 列表的格式
#2. 列表中可以嵌套任何类型
#通过list类创建的对象，li
li = [ 1,12,9," age" ,["哈哈哈"," 吼吼吼吼" ]," alex" ]
#中括号括起来
#，分割每个元素
#列表中的元素可以是 数字，字符串 列表，布尔值...所有的都能放进去
#“集合”，内部可以放置任何东西

#3. 索引取值
print(li[3])
#4. 切片，切片结果也是列表
print(li[3:5])
#5. for循环
#6. while 循环
for item in li :
    print(item)

#列表元素，可以被被修改

#7. 索引 修改
li[2] = 999999
print(li)
#7.1 索引    删除
del li[1]
print(li)
#8. 切片 修改2.0
li[1:3] = [55555555,"sjadhkjashd"]
print(li)
#8.1 切片 删除2.0
del li[2:4]
print(li)
#9.0 in 操作
li2 = [ 1,12,9," age" ,["哈哈哈"," 吼吼吼吼" ]," alex" ]
v = 12 in li2
print(v)
v1 = "哈哈哈" in li2
print(v1)

#10 操作
#索引特定元素
li3 = [1,12,9,"age",["哈哈哈",["19",10],"吼吼吼吼"],"alex"]
p = li3[4][1][0]
print(p)

#字符串 转换 列表
#字符串转化列表  li = list("djshakjdh") 内部使用for循环
s = "sajdhjashdkahskjdhska"
new_li = list(s)
print(new_li)
#列表 转换 字符串
#需要自己写for循环一个一个处理：既有数字又是字符串
li4 = [111,222,333,"123","alex"]
k = ""
for i in li4 :
    k = k + str(i)
print(k)
#列表 转换 字符串 2.0
#直接使用字符串join方法：列表的元素只有字符串
li5 = ["kldsa","jsajdjas"]
r = "".join(li5)
print(r)

for x in range(1,100//5):
    print(x)