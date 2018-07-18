tpp = "i am {},age {}, {}".format("seven",18,'alex')
print(tpp)

#不一一对应会报错
# tpp = "i am {},age {}, {}".format("seven",18)
# print(tpp)

ppp = "i am {2},age{1}, {0}".format("seven",18,'alex')
print(ppp)    #按照索引取值

kk = "i am {1},age {1}, ".format("seven",18,'alex')
print(kk)     #按照索引取值

koko = "i am {name} age{age} really {name}".format(name="alex",age=18)
print(koko)          #字典形式

koo = "i am {name} age{age} really {name}".format(**{"name":"alex","age":18})
print(koo)            #字典形式2.0   **字典

gg = "i am {0[0]} age{0[1]} really {1[2]}".format([1,2,3],[666,88,99])
print(gg)

gg = "i am {:s} age{:d} really {:f}".format("seven",18,88888.1)
print(gg)

nn = "i am {:s} age{:d} ".format(*["seven",18])
print(nn)             #  *列表

nb = "i am {:s} age{:d} ".format(*("seven",18))
print(nb)            #  *元组


zz = "i am {name:s} age{age:d} ".format(**{"name":"alex","age":18})
print(zz)

lo = "number : {:b},{:o},{:d},{:x},{:X}, {:%}".format(15,15,15,15,15,15)
print(lo)


