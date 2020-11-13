n = input("Enter a number: ")
if str(n) == str(n)[::-1]:
	print("This number is symmetrical ->", n)
else:
	print("This number isn't symmetrical ->", n)
