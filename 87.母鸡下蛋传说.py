# def xiadan():
#     ret = []
#     for i in range(100):
#         ret.append('鸡蛋%s' %i)
#     return ret
# print(xiadan())
#缺点一 ：占空间大
#缺点二 ：效率低

def xiadan():
    for i in range(100):
        yield '鸡蛋%s' %i

alex_lmj=xiadan()
jidan=alex_lmj.__next__()
jidan=alex_lmj.__next__()
jidan=alex_lmj.__next__()

print('xxx',jidan)