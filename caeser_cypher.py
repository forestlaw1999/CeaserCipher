from string import ascii_lowercase as letters 
# import ascii lowercase letters for alphabet
from termcolor import colored
# import colored text for error messages

# Function to encrypt plain text into cipher text using Caesar cipher 
def PlainToCipher(plain, alphabets:str, shift ):
    cipher_text = []
    for word in plain:
        cipher_word = '' 
        for letter in word:
            letter_position = alphabets.find(letter) 
            # get index of letter in alphabet
            rotation = (letter_position + int(shift)) % 26  
            # shift letter index by specified amount
            cipher_letter = alphabets[rotation]
            # get new shifted letter from alphabet 
            cipher_word += cipher_letter       
        cipher_text.append(cipher_word)
        cipher = ' '.join(cipher_text)
    return cipher        

# Function to decrypt cipher into plain text
def CipherToPlain(cipher,alphabets:str,shift):
    plain_text = []
    for word in cipher:
        plain_word = ''
        for letter in word:
            letter_index = alphabets.find(letter)
            rotation = (letter_index - shift)%26
            plain_letter = alphabets[rotation]
            plain_word += plain_letter
        plain_text.append(plain_word)
        plain = " ".join(plain_text)
    return plain

def PlainInput():
# Get plain text input from user         
    plain_text = input("Enter the text to encode: ").lower()
    while not plain_text.replace(" ","").isalpha():
        # Validate input contains only letters
        print(colored("Error!\nThe text should only contain alphabets. Try again.",'red')) 
        plain_text = input("Enter text to encode: ").lower()
    plain_text = plain_text.split(" ") 
    return plain_text

# Get cipher input from user
def CipherInput():
    cipher_text = input("Enter the text to decode: ").lower()
    while not cipher_text.replace(" ","").isalpha():
        # Validate input contains only letters
        print(colored("Error!\nThe text should only contain alphabets. Try again.",'red')) 
        cipher_text = input("Enter text to decode: ").lower()
    cipher_text = cipher_text.split(" ") 
    return cipher_text


# Get shift value from user
def ShiftValue():
    shift = input("Enter the shift value: ")
    while not shift.isdecimal():
        # Validate input is a number 
        print(colored("Invalid input. Try again.","red"))
        shift = input("Enter the shift value: ")
    shift = int(shift)
    return shift

choices = ['encode','decode']
print("\t\tWelcome to Ceaser Cypher\n")
choice = input("Enter 'encode' to encrypt or 'decode' to decrypt: ").lower()
while not choice in choices:
    print(colored("Invalid choice. Try again.",'red'))
    choice = input("Enter 'encode' to encrypt or 'decode' to decrypt: ")

shift = ShiftValue()

if choice == 'encode':
    plain_text = PlainInput()
    cipher = PlainToCipher(plain_text,letters,shift)
    print(cipher)
else:
    cipher_text = CipherInput()
    plain = CipherToPlain(cipher_text,letters,shift)
    print(plain)    
