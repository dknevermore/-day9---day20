python_l=['lcg','szw','zjw','lcg',2]
linux_l=['lcg','szw',1]
p_s = set(python_l)
l_s = set(linux_l)
print(p_s,l_s)
p_s.difference_update(l_s)  #差集，并更新
print(p_s)

# s1 = {1,2}
# s2 = {3,5}
# print(s1.isdisjoint(s2))  #是否无交集

s1 = {1,2}
s2 = {1,2,3,4}
print(s1.issubset(s2))    #s1是否是s2的子集
print(s2.issuperset(s1))  #s2是否是s1的父集

s1.update(s2)             #更新多个值
print(s1)