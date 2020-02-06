import zipfile
import os

alphabet = "$0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def to_alphabet(n):
    base = len(alphabet)
    result = ''
    while n > 0:
        rest = n % base
        result = alphabet[rest] + result
        n = n // base
        new = ''
    for i in range(0,len(result)):
        if result[i] != '$':
            new = new + result[i]
    return new
    
def next_password(state):
    result = to_alphabet(state)
    return result

with open('pop_passwords.txt') as f:
    passwords = [password.strip() for password in f.readlines()]
   
def next_password_smart(state):
    return passwords[state]


string = input("Enter the name of archieve: ")

key = int(input("""
Choose a method:
1) brute force smart
2) brute force
"""))

if (key != 1) and (key !=2):
    print('Error. Choose 1 or 2')
else:

    print("Start hacking...")
    direct = "Extracted from " + string
    os.mkdir(direct)

    word = ''
    state = 0
    
    while True:
        with zipfile.ZipFile(string, 'r') as z:
            z.setpassword(word.encode())
            try:
                z.extractall(direct)
            except:
                print(state+1, "[False]: " + word)
            else:
                print(state+1, "[True]: " + word)
                break
        state += 1    
        if key == 2:    
            word = next_password(state)
        elif key == 1:
            word = next_password_smart(state)
                      
    print()        
    print("Password: ", word)
    print()
    print("Extracting in <<", direct, ">>")
    print('Finished.')

print()
input("Tap Enter")
        
