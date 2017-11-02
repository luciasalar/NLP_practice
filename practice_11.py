
#num = str(num)


def first_last():
	num = input("input numbers:")
	new_list= []
	x= num[0]
	y= num[-1]
	new_list.append(x)
	new_list.append(y)
	return new_list

print(first_last())