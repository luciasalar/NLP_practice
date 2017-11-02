import json
from pprint import pprint

with open('birthday.json') as data_file:    
    birthday_dictionary = json.load(data_file)

#pprint(birthday_dictionary)


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