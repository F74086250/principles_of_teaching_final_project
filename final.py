play=input('Wanna start?y/n:')
while(play=='y'):
	animal=input("Input the kind of animal:")
	temperature=input("Input the temperature:")
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
