#read(3)代表读取3个字符
#其余的文件内光标移动都是以字节为单位如seek，tell，read，truncate

#f.flush()   #将文件内容从内存刷到硬盘
#f.closed    #文件如果关闭则返回True
#f.encoding  #查看使用open打开文件的编码
#f.tell()    #查看文件处理当前的光标位置
#f.seek(3)  #从开头开始算，将光标移动到第三个字节
# f.truncate(10)   #从开头开始算，将文件只保留从0-10个字节的内容
#文件必须以写方式打开，但是w和w+除外

'''
f = open('81seek.txt','r',encoding='utf-8')
print(f.tell())
f.seek(10,0)   #从文件开头数10个字节
print(f.tell())
f.seek(3,0)
print(f.tell())
'''
'''
f = open('81seek.txt','rb')
print(f.tell())
f.seek(10,1)   #相对上个光标的后10个字节
print(f.tell())
f.seek(3,1)
print(f.tell())
'''
#seek与日志有关

# f = open('81seek.txt','rb')
# print(f.tell())
# f.seek(-5,2)   #倒着seek  注意 一个汉字3个字节
# print(f.read())
# print(f.tell())
# #f.seek(3,1)
# #print(f.tell())

f = open('81日志文件','rb')
# data = f.readlines()
# print(data[-1].decode('utf-8'))

#循环文件的推荐方式
# for i in f:
#     print(i)



for i in f:
    offs=-10
    while True:
        f.seek(offs,2)
        data = f.readlines()
        if len(data)>1:
            print('文件的最后一行是%s' %(data[-1].decode('utf-8')))
            break
        offs*=2