'''
f = open('72陈粒','w',encoding='utf-8')
#如果文件存在则清空文件内容，如果文件不存在则创建新的文件
#即新建一个空文档覆盖之前的文档
#f.read()
f.write('111111111111\n')
f.write('222222222222222\n')
f.write('33\n44444\n5555\n')
#f.writable
f.writelines(['555555\n','6666666666\n'])
#f.write(3)    #报错   文件内容只能是字符串
f.close()
'''