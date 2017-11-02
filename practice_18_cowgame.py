import random


def cow_game():	
	num = random.randint(1000,9999)
	cowbull = [0,0] #cow then bull
	for i in str(num):  
		for j in str(guess_num):
			if  i == j:
				cowbull[0] +=1
			else:
				if i in j:
					cowbull[1] +=1
	return cowbull



if __name__=="__main__":
	while True:
		guess_num = input('input a number:')
		print(cow_game())


