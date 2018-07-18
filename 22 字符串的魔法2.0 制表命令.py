s = "1234567\t89"
v = s.expandtabs(6)
print(v,len(v))
#expandtabs,断句20，即每一组20格  一般用于制表
s1 ="username\temail\tpsaaword\nwodalao\twodalao@qq.com\t123456\n"
v1 = s1.expandtabs(20)
print(v1,len(v1))
