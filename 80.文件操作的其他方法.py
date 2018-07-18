# f = open('80a.txt','r',encoding='gbk')  #因为不知道编码所以会报错
# data = f.read()
# print(data)
# #print(f.closed) #文件如果关闭则返回True

#f = open('80b.txt','r+',encoding='utf-8',newline='')  #读取文件中真正的换行符号
f = open('80b.txt','r+',encoding='utf-8',newline='')  #读取文件中真正的换行符号
#print(f.closed) #判断是否关闭
#print(f.encoding)      #查看使用open打开文件的编码
#f.flush()  #将文件内容从内存刷到硬盘
#print(f.readlines())
# print(f.tell())
# f.readlines()
# print(f.tell())    #查看文件处理当前的光标位置
# # f.seek(1)
# # print(f.tell())
# # print(f.readlines())
# f.seek(3)          #从开头开始算，将光标移动到第三个字节
# print(f.tell())
# print(f.read())
# data = f.read(4)  #读字符
# print(data)

# f.truncate(10)   #从开头开始算，将文件只保留从0-10个字节的内容
#文件必须以写方式打开，但是w和w+除外

