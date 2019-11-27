import random
import re
import csv

def get_word_bank(file_name):
	word_bank = []
	file = open(file_name, 'r')
	reader = csv.reader(file, delimiter='\n')
	for line in reader:
		word_bank.append(line[0])
	# print(word_bank)
	return word_bank

def dummy_hangman(word):
	life_count = 10
	# print("You have %d lives, good luck!" % life_count)
	word_mask = []
	pattern = re.compile("[A-Za-z]")
	for i in word:
		if pattern.fullmatch(i) is not None:
			word_mask.append("_ ")
		else:
			word_mask.append("%s " % i)
	# print(word)
	# print(word_mask)
	# player_sees = ''
	# for i in word_mask:
	# 	player_sees = player_sees + i
	# print(player_sees)
	wrong_count = 0
	used_letters = []
	winner_winner_chicken_dinner = False
	while(wrong_count < life_count):
		print("||YOU HAVE %d LIVES||" % (life_count-wrong_count))
		print(word_mask)
		print(used_letters)
		guess = input("Guess a letter >>> ")
		print("\n")
		if (len(guess) != 1) or (pattern.fullmatch(guess) is None):
			print("||YOU KNOW, YOU MIGHT HAVE BETTER LUCK IF YOU PLAYED THE GAME RIGHT. TRY AGAIN||\n")
			continue
		if guess in used_letters:
			print("||YOU ALREADY USED THAT ONE||\n")
			continue
		used_letters.append(guess)
		if guess not in word:
			wrong_count = wrong_count + 1
			continue
		index = 0
		for i in word:
			if i.lower() == guess.lower():
				word_mask[index] = i
			index = index + 1
		if("".join(word_mask) == word):
			winner_winner_chicken_dinner = True
			break
	if winner_winner_chicken_dinner:
		print("||CONGRATULATIONS! YOU WON||")
	else:
		print("||YOU RAN OUT OF LIVES. THE WORD WAS %s! BETTER LUCK NEXT TIME. EXITING...||\n" % word)
	return

print("||WELCOME TO DUMMY HANGMAN||")
cat_select = ""
file_name = ""
while True:
	print("Animals (or enter 1)\tSports (or enter 2)\tHolidays (or enter 3)")
	cat_select = input("Please select a category from above >>> ")
	if (cat_select.lower() == 'animals') or (cat_select == '1'):
		print("\nYou selected Animals!\n")
		file_name = 'animals.txt'
		break
	elif (cat_select.lower() == 'sports') or (cat_select == '2'):
		print("\nYou selected Sports!\n")
		file_name = 'sports.txt'
		break
	elif (cat_select.lower() == 'holidays') or (cat_select == '3'):
		print("\nYou selected Holidays!\n")
		file_name = 'holidays.txt'
		break
	else:
		print("\nBruh type some actual words try again squadfam out\n")
word_bank = get_word_bank(file_name)
word = word_bank[random.randint(0, len(word_bank) - 1)]
# print(word)
dummy_hangman(word)
