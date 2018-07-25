class Addition():

	def __init__(self):
		num_1 = float(input ('some number: '))
		num_2 = float(input ('some number: '))
		self.res = num_1 + num_2
		return print(f'Addition of two number is {self.res}')

class Subtraction():

	def __init__(self):
		num_1 = float(input ('some number: '))
		num_2 = float(input ('some number: '))
		self.res = num_1 - num_2
		return print(f'Subtraction of two number is {self.res}')

class Multiplication():

	def __init__(self):
		num_1 = float(input ('some number: '))
		num_2 = float(input ('some number: '))
		self.res = num_1 * num_2
		return print(f'Multiplication of two number is {self.res}')

class Division():

	def __init__(self):
		num_1 = float(input ('some number: '))
		num_2 = float(input ('some number: '))
		self.res = num_1 / num_2
		return print(f'Division of two number is {self.res}')

n = input('What do you want to do? (+ - * /): ')

while n!='q':
	if n == '/':
		print('You choose division, now put some number/n')
		Division()
	elif n == '*':
		print('You choose multiplication, now put some number/n')
		Multiplication()
	elif n == '+':
		print('You choose addition, now put some number/n')
		Addition()
	elif n == '-':
		print('You choose subtraction, now put some number/n')
		Subtraction()
	else:
		print('You must put some action, not letter or number')

	n = input('What do you want to do? (+ - * /): ')