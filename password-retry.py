
password = 'a123456'
i = 3

while i > 0:
	pw = input('请输入密码：')
	i = i - 1
	if pw == password:
		print('登入成功！')
		break
	else:
		print('密码错误！')
		if i > 0:
			print('还有', i, '次机会')
		else:
			print('账号将被锁定')
