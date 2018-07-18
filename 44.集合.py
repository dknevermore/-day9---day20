s = set('hello')
print(s)

s1 = set(['alex','alex','sb'])
print(s1)

#添加   只能添加一个值
s3 = {1,2,3,4,5,6}
s3.add('s')
s3.add('3')
s3.add(3)
print(s3)

#清空
# s3.clear()
# print(s3)

#拷贝
s9 = s3.copy()
print(s9)

#随机删除
s12 = {'s',1,2,3,4,5,6}
s12.pop()
print(s12)
#指定删除
s13 = {'sb',1,2,3,4,5,6}
s13.remove('sb')  ##删除元素不存在会报错
print(s13)
#指定删除1.0
s14 = {'sbbbbb',1,2,3,4,5,6}
s14.discard('sbbbbb') #删除元素不存在不会报错
print(s14)