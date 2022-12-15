import random

# Set of letters to choose from
letters = "abcdefghijklmnopqrstuvwxyz"

# Set of numbers to choose from
numbers = "0123456789"

# Set of special characters to choose from
special_characters = "!@#$%^&*()_+-=[]{}|:;<>,.?/"

# Function to generate a password
def generate_password(length):
  # Start with an empty password
  password = ""
  
  # Add a random letter to the password
  password += random.choice(letters)
  
  # Add a random number to the password
  password += random.choice(numbers)
  
  # Add a random special character to the password
  password += random.choice(special_characters)
  
  # Add remaining random characters to the password
  for i in range(length-3):
    password += random.choice(letters + numbers + special_characters)
  
  # Shuffle the password to add an extra level of randomness
  password = ''.join(random.sample(password, len(password)))
  
  # Return the generated password
  return password

# Function to evaluate the password strength
def evaluate_password(password):
  # Initialize the password strength to 0
  strength = 0
  
  # If the password is at least 8 characters long, add 1 to the strength
  if len(password) >= 8:
    strength += 1
  
  # If the password includes at least one letter, one number, and one special character, add 1 to the strength
  if any(char.isdigit() for char in password) and any(char.isalpha() for char in password) and any(char in special_characters for char in password):
    strength += 1
  
  # Return the password strength
  return strength

# Prompt the user for the password length
length = int(input("Enter the password length: "))

# Generate and print the password
password = generate_password(length)
print("Your password is:", password)

# Evaluate and print the password strength
strength = evaluate_password(password)
print("Password strength:", strength)
