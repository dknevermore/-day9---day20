##f = open('78test1.py','rb',encoding='utf-8') #b的方式不能指定编码
# f = open('78test1.py','rb')
# data = f.read()
# #'字符串'----------------- encode ------------------> bytes
# #bytes-------------------  decode ----------------->'字符串'
# print(data)  #window中、  \r\n   就代表回车
# print(data.decode('utf-8'))
# f.close()

# f = open('79test22.py','wb')
# f.write(bytes('111111111111\n',encoding='utf-8'))
# f.write('杨戬'.encode('utf-8'))

# f = open('79test22.py', 'ab')
# f.write('杨戬'.encode('utf-8'))

