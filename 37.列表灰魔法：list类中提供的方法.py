#########灰魔法：list类中提供的方法##########3
#列表是有序的，元素可以被修改
#对象.方法（...)  例：li对象使用append方法
li = [11,22,33,44]
#参数

#追加
#1.原来值最后追加
li.append(5)
li.append("alex")
li.append([1234,54654])
print(li)

#2.清空列表
li2 = [111,521,54442]
li2.clear()
print(li2)

#3. 拷贝 ,浅拷贝
v = li.copy()
print(v)

#4.计算元素出现的次数
v2 = li.count(22)
print(v2)

#5.扩展原列表 参数：可迭代对象
li3 = [11,22,33,44]
li3.extend([9898,"不得了"])
print(li3)
li3.extend("不得了")
print(li3)

#6.根据值获取当前值索引位置（左边优先）
li4 = [11,22,33,22,44]
q = li4.index(22)
print(q)
#7.指定索引位置插入元素
li4.insert(0,999)
print(li4)
#index表示索引  value表示值

#8.删除某个值，并获取删除的值
#若不加参数则表示删除最后一个元素
li5 = [11,22,33,44]
e = li5.pop(1)
print(li5)
print(e)
#9.删除列表中的指定值，左边优先
li6 = [11,22,33,22,44]
li6.remove(33)
print(li6)
#删除命令Ps : pop   remove  del li[0]   del li[7:9]   clear

#10.将当前列表进行翻转
li7 = [11,22,33,22,44]
li7.reverse()
print(li7)

#11.列表的排序
li8 = [11,99,66,33,55,77]
li8.sort()
print(li8)
li9 = [11,99,66,33,55,77]
li9.sort(reverse= True)
print(li9)
###欠
#cap
#key
#sorted
for i in range(1,10):
    print(i)