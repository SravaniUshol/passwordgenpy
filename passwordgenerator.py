import string
import random

def generate_password(length):
    # Define possible characters: uppercase, lowercase, digits, and special characters
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

def main():
    print("Password Generator")
    
    try:
        # Prompt the user to specify the desired length of the password
        length = int(input("Enter the desired length of the password: "))
        
        if length <= 0:
            print("Error: Password length should be greater than 0.")
            return
        
        # Generate the password
        password = generate_password(length)
        
        # Display the generated password
        print(f"Generated password: {password}")
    
    except ValueError:
        print("Error: Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()
