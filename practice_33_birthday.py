birthday_dictionary = {
	"Albert Einstein": "03/14/1879",
	"Benjamin Franklin": "01/17/1706",
	"Ada Lovelace": "10/12/1815",

}

if __name__=="__main__":
	print("Welcome to the birthday dictionary. We know the birthdays of:")
	for key in birthday_dictionary:
		print ((key))

	
	b_name = input("Who's birthday do you want to look up?")

	def birthday():
		for key in birthday_dictionary:
			if b_name == key:
				return birthday_dictionary[key]
	print (birthday())


