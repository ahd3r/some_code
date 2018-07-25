#pip install simple draw

import simple_draw as sd
from random import randint

less_length = 0
less_angle = 0

'''
dick
'''

vector = sd.get_vector(sd.get_point(250, 0), 90, 30, 1)
vector.draw()

for bell_1 in range(27):
	vector = sd.get_vector(vector.end_point, -135-10*bell_1, 15, 1)
	vector.draw()

vector = sd.get_vector(vector.end_point, 90, 300, 1)
vector.draw()

for end in range(11):
	vector = sd.get_vector(vector.end_point, 90-15*end, 20, 1)
	vector.draw()

vector = sd.get_vector(sd.get_point(350, 0), 90, 30, 1)
vector.draw()

for bell_1 in range(25):
	vector = sd.get_vector(vector.end_point, -45+10*bell_1, 15, 1)
	vector.draw()

vector = sd.get_vector(vector.end_point, 90, 320, 1)
vector.draw()

'''
spiral
'''

# vector = sd.get_vector(sd.get_point(10,0),90,50,1)
# vector.draw()

# for x in range(0, 5):
# 	vector = sd.get_vector(vector.end_point, 90, 50, 1)
# 	vector.draw(color=sd.COLOR_PURPLE)

# for y in range(0, 100):
# 	less_length = less_length + 0.6
# 	less_angle = less_angle + 15
# 	vector = sd.get_vector(vector.end_point, 90 - less_angle, 60 - less_length, 1)
# 	vector.draw(color=sd.COLOR_CYAN)

sd.pause()