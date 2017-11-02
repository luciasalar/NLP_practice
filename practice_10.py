def get_prime():
	return int(input("give me a numnber:"))

num = get_prime()
if num % 2 != 0:
	print ("It's a prime!")
else:
	print("It's an even!")

