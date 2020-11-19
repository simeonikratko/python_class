str = input("Enter string: ")


def lenstr(str): 
	count = 0	
	for i in str: 
		count += 1
	return count

print(lenstr(str))