def reverse():
	text = input("input some text:")
	result = text.split()
	return result[::-1]

print (reverse())