import math
def root():
	x = input('Enter a number: ')
	x_int = int(x)
	counter = 0
	while x_int > 2:
		counter = 0
		math.sqrt(x_int)
		counter += 1
	print(x_int)
	print(counter)
print(root())




