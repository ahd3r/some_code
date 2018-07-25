import simple_draw as sd
from random import randint

sd.resolution = (700, 700)

def brench(start_point, angle, length, delta_angle=50):

	if length < 5:
		return
	width = 4
	if length < 40:
		width = 1
	elif length < 100:
		width = 2

	vector = sd.get_vector(start_point = start_point, angle = angle, length = length, width = width)
	vector.draw(sd.random_color())
	brench(start_point = vector.end_point, angle = angle - (delta_angle + randint(10,20)), length = length * (randint(60,80) / 100), delta_angle = delta_angle)
	brench(start_point = vector.end_point, angle = angle + (delta_angle + randint(10,20)), length = length * (randint(60,80) / 100), delta_angle = delta_angle)

brench(sd.get_point(300, 0), 90, 200, 10)

sd.pause()