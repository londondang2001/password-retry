password = 'a123456'	# 密码
i = 3	# 剩余机会

while True:		# 重复输入
	pw = input('请输入密码：')
	if pw == password:		# 如果 就
		print('登入成功！')
		break
	else:		# 否则
		i = i - 1
		print('密码错误！还有', i, '次机会')
		if i == 0:		# 如果 就
			break


