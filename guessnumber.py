import random
start = int(input('請輸入開始數字: '))
end = int(input('請輸入結束數字: '))
r = random.randint(start, end)
count = 0
while True:
	count += 1
	num = int(input('請輸入數字: '))
	if num == r:
		print('你猜對了!')
		print('你總共猜了', count, '次')
		break
	elif num > r:
		print('你輸入的數字大於答案')
	elif num < r:
		print('你輸入的數字小於答案')
	print('你總共猜了', count, '次')