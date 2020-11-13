str1 = input("Please enter a word: ")

x = 0

vowels = ['a', 'e', 'o', 'u', 'i']

for i in str1:
    if i.lower() in vowels:
        x += 1

print("Number of vowels in the string ->", x)