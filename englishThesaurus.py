import json
from difflib import get_close_matches, SequenceMatcher

data = json.load(open("data.json"))

def translate(word):
	word = word.lower()
	word_list = get_close_matches(word, data.keys())

	if word in data:
		return data[word]
	elif word.title() in data.keys():
		return data[word.title()]
	elif word.upper() in data.keys():
		return data[word.upper()]
	elif len(get_close_matches(word, data.keys())) > 0:
		word = word_list[0]
		confirmation = input("Did you mean {}? Type Y or N: ".format(word))
		if confirmation.lower() == "y":
			return data[word]
		elif confirmation.lower() == "n":
			return "This word does not exist. Please try again."
		else:
			return "We didn't understand your entry."
	else:
		return "This word does not exist. Please try again."

word = input("Please enter a word: ")
output = translate(word)

for i in output:
	if isinstance(output, list):
		print (i)
	else:
		print(output)
		break