import random
import string
def generate_random_password(length):
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation
    all_characters = uppercase + lowercase + digits + special_characters
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_characters)
    ]
    password += random.choices(all_characters, k=length - 4)
    random.shuffle(password)
    return ''.join(password)

password_length = int(input("Enter the length of the password:"))
print("Generated Password:", generate_random_password(password_length))
