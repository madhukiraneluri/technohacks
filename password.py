import random
import string

def generate_password(length):
    password=[]
    characters = string.ascii_letters + string.digits + string.punctuation
    for i in range(10):
        password.append(''.join(random.choice(characters) for _ in range(length)))
    return password

# Example usage
if __name__ == "__main__":
    length = int(input("Enter the length of the password: "))
    password = generate_password(length)
    [print(i+1,".",password[i]) for i in range(10)]
    choice=int(input("ENTER THE NUMBERS FROM 1 to 10 :"))
    if choice in range(1,11):
        print("Generated Password:", password[choice])
    else:
        print("INVALID!!")
