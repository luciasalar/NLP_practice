import json
from pprint import pprint

with open('birthday.json') as data_file:    
    birthday_dictionary = json.load(data_file)

#pprint(birthday_dictionary)