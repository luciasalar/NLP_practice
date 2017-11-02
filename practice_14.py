def new_list():
	num = [int(x) for x in input("input some numbers:")]
	return num

num = new_list()

def new_set(num):
	num2 = set()
	for i in num:
		num2.add(i)
	return num2

print (new_set(num))