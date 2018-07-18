s = 0
n = 1
while n < 101 :
	if n % 2 != 0 :
		s = s + n
		n = n + 1
	else :
		s = s - n
		n = n + 1
print(s)