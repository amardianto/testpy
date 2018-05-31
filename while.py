import random

running = True
jawaban = random.randint(0,5)

while running == True:
	tebak = int(input("Ketik angka: "))
	if tebak == jawaban:
		print("Selamat! Kamu benar.")
		break
	elif tebak < jawaban:
		print("Kekecilan")
	else:
		print("Kebesaran")
print("Permainan selesai")
	
