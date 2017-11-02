from random import randint

num = int(input("guess a number:"))

ran_num = randint(0, 9)

if num == ran_num:
	print ("you are right!")
else:
	print ("you are wrong!")



