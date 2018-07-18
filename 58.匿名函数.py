#  lambda x:x+1   匿名函数  x是形参 ：表达式      非常重要*****
#   匿名函数不能加复杂的关系
'''
def calc(x):
    return x+1

res = calc(10)
print(res)

print(lambda x:x+1)
func=lambda x:x+1
print(func(10))
'''

'''
name = "alex"
def change_name(x) :
    return name+"_sb"

res = change_name(name)
print(res)

'''
name = "alex"
f = lambda x: x+'_sb'
res = f(name)
print("匿名函数的运行结果",res)