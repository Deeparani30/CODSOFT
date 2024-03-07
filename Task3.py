import random
import string

def generate_password(length, complexity):
    characters = ""
    
    if 'lowercase' in complexity:
        characters += string.ascii_lowercase
    if 'uppercase' in complexity:
        characters += string.ascii_uppercase
    if 'digits' in complexity:
        characters += string.digits
    if 'punctuation' in complexity:
        characters += string.punctuation

    if not characters:
        print("Please select at least one complexity option.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired password length: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if length <= 0:
        print("Password length should be greater than 0.")
        return

    complexity_options = ['lowercase', 'uppercase', 'digits', 'punctuation']
    complexity = input("Enter the desired complexity options (comma-separated, e.g., lowercase,uppercase,digits): ").lower().split(',')

    password = generate_password(length, complexity)
    if password:
        print("Generated Password:", password)

if __name__ == "__main__":
    main()
