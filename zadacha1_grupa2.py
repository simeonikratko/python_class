a = input("Please enter the value of a: ")
b = input("Please enter the value of b: ")
c = input("Please enter the value of c: ")

def is_equal(a, b, c):
	if a[-1] * b[-1] == c[-1]:
		print('True')
	else:
	    print('Flase')
	 
	 
is_equal(a, b, c)