import random
import string

def generate_password(length):
    """Generate a random password of specified length"""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Prompt the user for the desired password length
length = int(input("Enter the length of the password: "))

# Generate the password
password = generate_password(length)

# Print the password
print("Your password is:", password)
