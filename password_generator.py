import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


password = ''
randomised_password = []

for letter in range(1, nr_letters+1):
    random_char = random.choice(letters)
    randomised_password.append(random.choice(letters))
    # randomised_password += random_char
for symbol in range(1, nr_symbols + 1):
    randomised_password.append(random.choice(symbols))
    # randomised_password += random.choice(symbols)
for number in range(1, nr_numbers + 1):
    randomised_password.append(random.choice(numbers)) 
    # randomised_password += random.choice(numbers)
    
random.shuffle(randomised_password)

for character in randomised_password:
    password += character
    
print(password)