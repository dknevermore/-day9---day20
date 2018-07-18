python_l=['lcg','szw','zjw','lcg',2]
linux_l=['lcg','szw',1]

#如果只想简单的执行去重操作，不考虑数据类型的顺序
#set() 就可以
p_s = set(python_l)
l_s = set(linux_l)
print(p_s,l_s)
#求交集
print(p_s.intersection(l_s))  #交集
print(p_s&l_s)                #交集1.0

#求并集
print(p_s.union(l_s))         #并集
print(p_s | l_s)              #并集1.0

#求差集
print(p_s.difference(l_s))     #差集
print("差集",p_s-l_s)          #差集
print(l_s.difference(p_s))     #差集
print("差集",l_s-p_s)          #差集

#交叉补集
print("交叉补集",p_s.symmetric_difference(l_s))  #交叉补集
print(p_s^l_s)                                   #交叉补集