import random
import string

# Function to generate a random password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to save the generated password to a file
def save_password_to_file(password):
    with open("password.txt", "w") as file:
        file.write(password)

# Main function
def main():
    length = int(input("Enter the length of the password (default is 12): "))
    password = generate_password(length)
    
    print("Generated Password:", password)
    
    save_option = input("Do you want to save this password to a file? (yes/no): ").lower()
    if save_option == "yes":
        save_password_to_file(password)
        print("Password saved to 'password.txt'")
    else:
        print("Password not saved.")

if __name__ == "__main__":
    main()
