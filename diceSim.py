import random

def d4(roll_count):
	rolls = []
	sum = 0
	max = 0
	min = 101
	avg = 0
	for i in range(roll_count):
		x = random.randint(1, 4)
		sum = sum + x
		rolls.append(x)
		if x > max:
			max = x
		if x < min:
			min = x
	print("You rolled %d d4s" % roll_count)
	print(rolls)
	avg = sum / roll_count
	print("Roll Sum: %d\tMax Roll: %d\tMin Roll: %d\tAvg Roll: %d" % (sum, max, min, avg))
	return

def d6(roll_count):
	rolls = []
	sum = 0
	max = 0
	min = 101
	avg = 0
	for i in range(roll_count):
		x = random.randint(1, 6)
		sum = sum + x
		rolls.append(x)
		if x > max:
			max = x
		if x < min:
			min = x
	print("You rolled %d d6s" % roll_count)
	print(rolls)
	avg = sum / roll_count
	print("Roll Sum: %d\tMax Roll: %d\tMin Roll: %d\tAvg Roll: %d" % (sum, max, min, avg))
	return

def d8(roll_count):
	rolls = []
	sum = 0
	max = 0
	min = 101
	avg = 0
	for i in range(roll_count):
		x = random.randint(1, 8)
		sum = sum + x
		rolls.append(x)
		if x > max:
			max = x
		if x < min:
			min = x
	print("You rolled %d d8s" % roll_count)
	print(rolls)
	avg = sum / roll_count
	print("Roll Sum: %d\tMax Roll: %d\tMin Roll: %d\tAvg Roll: %d" % (sum, max, min, avg))
	return

def d10(roll_count):
	rolls = []
	sum = 0
	max = 0
	min = 101
	avg = 0
	for i in range(roll_count):
		x = random.randint(1, 10)
		sum = sum + x
		rolls.append(x)
		if x > max:
			max = x
		if x < min:
			min = x
	print("You rolled %d d10s" % roll_count)
	print(rolls)
	avg = sum / roll_count
	print("Roll Sum: %d\tMax Roll: %d\tMin Roll: %d\tAvg Roll: %d" % (sum, max, min, avg))
	return

def d12(roll_count):
	rolls = []
	sum = 0
	max = 0
	min = 101
	avg = 0
	for i in range(roll_count):
		x = random.randint(1, 12)
		sum = sum + x
		rolls.append(x)
		if x > max:
			max = x
		if x < min:
			min = x
	print("You rolled %d d12s" % roll_count)
	print(rolls)
	avg = sum / roll_count
	print("Roll Sum: %d\tMax Roll: %d\tMin Roll: %d\tAvg Roll: %d" % (sum, max, min, avg))
	return

def d20(roll_count):
	rolls = []
	sum = 0
	max = 0
	min = 101
	avg = 0
	for i in range(roll_count):
		x = random.randint(1, 20)
		sum = sum + x
		rolls.append(x)
		if x > max:
			max = x
		if x < min:
			min = x
	print("You rolled %d d20s" % roll_count)
	print(rolls)
	avg = sum / roll_count
	print("Roll Sum: %d\tMax Roll: %d\tMin Roll: %d\tAvg Roll: %d" % (sum, max, min, avg))
	return

def d100(roll_count):
	rolls = []
	sum = 0
	max = 0
	min = 101
	avg = 0
	for i in range(roll_count):
		x = random.randint(1, 100)
		sum = sum + x
		rolls.append(x)
		if x > max:
			max = x
		if x < min:
			min = x
	print("You rolled %d d100s" % roll_count)
	print(rolls)
	avg = sum / roll_count
	print("Roll Sum: %d\tMax Roll: %d\tMin Roll: %d\tAvg Roll: %d" % (sum, max, min, avg))
	return



print("Welcome to Dice Simulator!")

while True:
	print("Please select which dice you'd like to roll\n\td4\n\td6\n\td8\n\td10\n\td12\n\td20\n\td100")
	dice = input("Select dice from list: ")
	# print("How many dice would you like to roll?")
	roll_count = 0
	while True:
		string = input("How many dice would you like to roll: ")
		try:
			roll_count = int(string)
			if roll_count < 0:
				raise NotPositiveError
			break
		except ValueError:
			print("Didn't your mom ever teach what a number is? Try again.")
		except NotPositiveError:
			print("How on earth am I supposed to roll that number of dice? Try again.")

	# if type(roll_count) != :
	# 	print("Come on now, that's not a fkn number! Try again")
	# 	continue

	print("")
	if dice == 'd4':
		d4(roll_count)
	elif dice == 'd6':
		d6(roll_count)
	elif dice == 'd8':
		d8(roll_count)
	elif dice == 'd10':
		d10(roll_count)
	elif dice == 'd12':
		d12(roll_count)
	elif dice == 'd20':
		d20(roll_count)
	elif dice == 'd100':
		d100(roll_count)
	else:
		print("Invalid dice selection. Try again")
	print("")