print('歡迎使用生物數據庫，目前可查詢的物種為:')
print("\n")
print('綠蠵龜		(學名:Chelonia mydas)')
print('佛州穴龜	(學名:Gopherus polyphemus)')
print('赤蠵龜		(學名:Caretta caretta)')
print('美國短吻鱷	(學名:alligator mississippiensis)')
print('待補充...')
print("==============================")
judge=input('要開始請輸入y，若要結束請輸入n:')
while(judge=='y'):
	animal=input('請輸入欲查詢的物種(輸入中文名就好):')
	temperature=input('出生時的溫度:')
	temperature=float(temperature)
	if animal=='綠蠵龜':
		if temperature>=30.0:
			print("為雌性的機率大於50%")
		else:
			print("為雄性的機率大於50%")

	elif animal=='佛州穴龜':
		if temperature>=29.3:
			print("為雌性的機率大於50%")
		else:
			print("為雄性的機率大於50%")

	elif animal=='赤蠵龜':
		if temperature>=29.2:
			print("為雌性的機率大於50%")
		else:
			print("為雄性的機率大於50%")

	elif animal=='美國短吻鱷':
		if temperature<=30.5:
			print('必為雌性')
		elif temperature==32.5 or temperature==33 or temperature==36:
			print('必為雄性')
		else:
			print('不一定')
	else:
		print('目前這個python生物數據庫暫時還沒有這個物種可供查詢')
	judge=input('要繼續請輸入y，若要結束請輸入n:')
	print('\n')
print('感謝您使用本python數據庫，更強大的搜尋功能正等待您的拓展!')


