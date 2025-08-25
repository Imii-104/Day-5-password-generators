import random 
print("Welcome to the Py Password Generator!")

user_letters = int(input("How many letters do you want your password to have?\n"))

user_numbers = int(input("How many numbers do you want your password to have?\n"))

user_symbols = int(input("How many symbols do you want your password to have?\n"))

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

# LETTERS GENERATION
random_letters = []
for L in range(user_letters):
    p_letters = random.choice(letters)
    random_letters.append(p_letters)
# print(random_letters)

# NUMBERS GENERATION
random_numbers = []
for N in range(user_numbers):
    p_numbers = random.choice(numbers)
    random_numbers.append(p_numbers)
# print(random_numbers)

# SYMBOLS GENERATION
random_symbols= []
for S in range(user_symbols):
    p_symbols = random.choice(symbols)
    random_symbols.append(p_symbols)
# print(random_symbols)
combined = "". join(random_letters + random_numbers + random_symbols)
print(combined)