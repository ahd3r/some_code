from random import randint


class Cat:

	def __init__(self, name):
		self.name 		= name
		self.mood 		= 100
		self.fulness 	= 50
		self.home		= None
		self.sleep		= 100

	def __str__(self):
		if self.home is None:
			if self.sleep >= 75:
				return f'I am a {self.name}, I am {self.mood}% good, I am full on {self.fulness}%, I don`t want to sleep ({self.sleep}%) and i am a stranger'
			if self.sleep >= 50:
				return f'I am a {self.name}, I am {self.mood}% good, I am full on {self.fulness}%, I want to sleep a little bit ({self.sleep}%) and i am a stranger'
			if self.sleep >= -200:
				return f'I am a {self.name}, I am {self.mood}% good, I am full on {self.fulness}%, I want to sleep ({self.sleep}%) and i am a stranger'
		else:
			if self.sleep >= 75:
				return f'I am a {self.name}, I am {self.mood}% good, I am full on {self.fulness}%, I don`t want to sleep ({self.sleep}%)'
			if self.sleep >= 50:
				return f'I am a {self.name}, I am {self.mood}% good, I am full on {self.fulness}%, I want to sleep a little bit ({self.sleep}%)'
			if self.sleep >= -200:
				return f'I am a {self.name}, I am {self.mood}% good, I am full on {self.fulness}%, I want to sleep ({self.sleep}%)'

	def eat(self):
		print(f'Food was teasty')
		self.fulness += 20
		self.sleep -= 10
		self.mood += 20

	def zzzz(self):
		print(f'I was dreaming')
		self.fulness -= 10
		self.sleep += 20
		self.mood -= 20

	def walk(self):
		print(f'Finaly, I am at home')
		self.sleep -= 10
		self.fulness -= 10
		self.mood += 20

	def in_home(self):
		if self.home is None:
			house = Home(full_of_bawl = 100)
			self.home = house
			print(f'I, {self.name}, settle in the house')
		else:
			print(f'Go back at your house')

	def act(self):
		dice = randint(1, 3)
		if dice == 1:
			self.eat()
		if dice == 2:
			self.zzzz()
		if dice == 3:
			self.walk()


class Home:

	def __init__(self, full_of_bawl):
		self.bawl = full_of_bawl


bob = Cat(name = 'Bob')
print(bob)
bob.eat()
print(bob)
bob.zzzz()
print(bob)
bob.in_home()
print(bob)

for day in range(1, 31):
	print(f'********************{day}')
	if bob.sleep <= 40:
		bob.zzzz()
		print(f'{bob.name} forced to sleep')
	if bob.fulness <= 20:
		bob.eat()
		print(f'{bob.name} forced to eat')
	if bob.mood <= 40:
		bob.walk()
		print(f'{bob.name} forced to walk')
	else:
		bob.act()
		print(bob)