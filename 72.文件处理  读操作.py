#文件处理流程

#1. 打开文件，得到文件句柄并赋值给一个变量
#f=open('a.txt','r',encoding='utf-8') #默认打开模式就为r

#2. 通过句柄对文件进行操作
#data=f.read()

#3. 关闭文件
#f.close()

#r读 w写 a追加
# f = open('72陈粒','r',encoding='utf-8')
# data = f.read()
# print(data)
#
# print(f.readable())   #文件是否可读
#
# print('第1行',f.readline())  #一次读一行  但如果前面有  data = f.read() 则f.readline()内容为空，因为在之前都读完了
# print('第2行',f.readline(),end='')   #去除回车，即空一行
# print('第3行',f.readline())
# print('第4行',f.readline())
# print('第5行',f.readline())
# print('第6行',f.readline())
# print('第7行',f.readline())
#
# data = f.readlines()
# print(data)
#
# f.close()


'''
f=open('xxx')       #因为‘xxx’文件设置是gbk编码  
data = f.read()     #window 默认的编码是gbk
print(data)
'''
#读出来的内容也只能是字符串