import random
import string

def generate_password(length, use_uppercase, use_digits, use_special):
    # Create a character pool based on user preferences
    characters = string.ascii_lowercase  # Start with lowercase letters

    if use_uppercase:
        characters += string.ascii_uppercase  # Add uppercase letters
    if use_digits:
        characters += string.digits  # Add digits
    if use_special:
        characters += string.punctuation  # Add special characters

    # Ensure there's at least one character type selected
    if not characters:
        print("Error: You must select at least one character type.")
        return None

    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    # Prompt user for password length
    length = int(input("Enter the desired length of the password: "))
    
    # Prompt user for password complexity options
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    # Generate the password
    password = generate_password(length, use_uppercase, use_digits, use_special)

    # Display the generated password
    if password:
        print(f"\nGenerated password: {password}")

# Entry point of the program
if __name__ == "__main__":
    main()
