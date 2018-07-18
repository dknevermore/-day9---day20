#这能根据换行分割   可以加参数True 或者 False 是否保留换行
test = "kajsdfkljakldfj\nakldsjflkajd\nkalsfjlkasjk\n"
v = test.splitlines()
print(v)

#查看是否...为开头 /  结尾
li = "backend 1.1.1.1"
v1 = li.startswith('ba')
print(v1)
v2 = li.endswith('1')
print(v2)

#大写变小写  小写变大写  大小写转换
da = "KSAJJdlskjdkladsakj"
v3 = da.swapcase()
print(v3)

