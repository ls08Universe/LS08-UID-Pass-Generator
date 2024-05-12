import random
import string
ascii_art = """

┓ ┏┓┏┓┏┓  ┳┳                ┏┓  ┏┓            ┓  ┏┓               
┃ ┗┓┃┫┣┫  ┃┃┏┏┓┏┓┏┓┏┓┏┳┓┏┓  ┣╋  ┃┃┏┓┏┏┓┏┏┏┓┏┓┏┫  ┃┓┏┓┏┓┏┓┏┓┏┓╋┏┓┏┓
┗┛┗┛┗┛┗┛  ┗┛┛┗ ┛ ┛┗┗┻┛┗┗┗   ┗┻  ┣┛┗┻┛┛┗┻┛┗┛┛ ┗┻  ┗┛┗ ┛┗┗ ┛ ┗┻┗┗┛┛ 
                                                                  

"""

def generate_username():
    username = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    return username

def generate_password():
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(password_characters, k=12))
    return password

def main():
    print(ascii_art)
    while True:
        username = generate_username()
        password = generate_password()
        print("\nGenerated Username:", username)
        print("Generated Password:", password)
        choice = input("\nDo you want to generate another username and password? (y/n): ").lower()
        if choice != 'y':
            break
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
