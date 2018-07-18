############整理############

#一、数字
#int(..)

#二、字符串
#replace/find/join/strip/startswith/split/upper/lower/format
tempalte = "i am {name},age :{age}"
v = tempalte.format(name='alex',age=19)
v1 = tempalte.format(**{"name":'alex','age':19})
print(v)
print(v1)

#三、列表
#append、extend、insert
#索引，切片，循环

#四、元组
#忽略
#索引，切片，循环   以及元素不能被修改

#五、字典
#get/update/keys/values/items
#for，索引

#六、布尔值
#0  1
#bool(...)
#None  "" ()  []  {} ==>False