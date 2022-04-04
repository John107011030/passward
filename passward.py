#密碼重試專案
#passward = 'a123456'
#請使用者重複輸入密碼
#最多3次
#正確的話就印出登入成功
#失敗的話就印出密碼錯誤！還有_次機會
passward = 'a123456'
x = 3 #總次數
while True:
	pwd = input('請輸入密碼：')
	#↑為了避免因為名稱重疊而導致資料被覆蓋，故這裡使用簡寫
	if pwd == passward:
		print('登入成功')
		break
	else:
		x = x - 1
		print('密碼錯誤！還有', x,'次機會' )
		if x == 0:
			break