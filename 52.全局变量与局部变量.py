name='lhf'  #全局变量

def change_name():
    #global name  局部变量变成全局变量
    name = "帅的一比"  #局部变量
    print('change_name',name)
change_name()
print(name)
#如果函数的内容无global关键字，优先读取局部变量，能读取全局变量，无法对全局变量重新赋值 NAME="fff"
#但是对于可变类型，可以对内部元素进行操作
#如果函数中有global关键字，变量本质上就是全局的那个变量，可读取可赋值 NAME = "fff"
NAME = ['我好帅啊',"哈哈哈哈"]

def change_NAME():
    NAME.append("大哥大哥")
    print('change_NAME',NAME)
change_NAME()
print(NAME)

######## 全局变量变量名大写
######## 局部变量变量名小写
