play=input('要開始或繼續請輸入y，若要結束請輸入n:')
while(play=='y'):
	animal=input("輸入一個動物:")
	temperature=input("輸入出生時的溫度:")
	#print(type(animal),type(temperature))
	temperature=int(temperature)
	if animal=='松獅蜥':
		if 22<temperature<34:
			print('雌雄數目相當')
		elif temperature>=34:
			print('大多數為雌性')
		else:
			print('文本中並未詳細說明')

	elif animal=='美國短吻鱷':
		if 29<=temperature and temperature<=31:
			print('主要為雌性')
		elif 32<=temperature and temperature<=34:
			print('主要為雄性')
		else: 
			print('文本中並未詳細說明')
	play=input('Wanna start?y/n')
print('finish!!')
