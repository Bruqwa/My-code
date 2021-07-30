import random

def generator():
	upperLetters = 'ABCDEFGHIJKLOPQRSTUVWXYZ'
	lowerLetters = 'abcdefghijklopqrstuvwxyz'
	numbers = '0123456789'
	symbols = '!@#$%^&*()[]:;"?><,.-_+='

	chars = upperLetters + lowerLetters + numbers + symbols
	allchars = []
	for i in chars:
		allchars.append(i)
	random.shuffle(allchars)

	length = int(input("Enter password length (should be more then 4): "))

	password = []
	password.append(random.choice(upperLetters))
	password.append(random.choice(lowerLetters))
	password.append(random.choice(numbers))
	password.append(random.choice(symbols))

	if len(password) <= length:
		saltlen = length - len(password)
	else:
		saltlen = 0
	password.extend(random.choices(allchars, weights=None, cum_weights=None, k=saltlen))
	random.shuffle(password)
	password = ''.join(password)

	return password
