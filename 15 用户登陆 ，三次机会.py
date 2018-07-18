n = 0
print('用户')
while n < 3 :
	inp = int (input('请输入6位密码'))
	if inp != 123456 :
		print('密码错误')
		n = n + 1
	else :	
		print('登入成功')
		break  