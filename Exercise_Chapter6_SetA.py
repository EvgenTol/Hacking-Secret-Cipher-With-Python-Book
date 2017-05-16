'''
Book: Hacking Secret Ciphers with Python, by Al Sweigart
Author: Evgen Tolstykh

Page: 72
Chapter: 6
Set: A

'''

#import pyperclip

#String to be encrypted/decrypted
message = "This is my secret Message"

#Key for encryption/decryption
key = 13

# Tells the programm to encrypt or decrypt
mode = "encrypt"

# Every possible symbols that can be encrypted
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# stores the encrypted/decrypted form of the message
translated = ""
# Capitalize the string in message
message = message.upper()

# Run the encryption/decryption code on each symbol in the message string
for symbol in message:
    if symbol in LETTERS:
        #get the encrypted/decrypted number for this Symbol
        num = LETTERS.find(symbol) #get the number of the symbol
        if mode == "encrypt":
            num = num + key
        elif mode == "decrypt":
            num = num - key

        # handle the wrap-around if num is larger than the length of LETTERS or less than 0
        if num >= len(LETTERS):
            num = num - len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)

        #add encrypted/decrypted numbers symbol at the end of translated
        translated = translated + LETTERS[num]
    else:
        # just add the symbol without encrypting/decrypting
        translated = translated + symbol

#print the encrypted/decrypted string to the screen
print(translated)

# copy the encrypted/decrypted string to the clipboard
#pyperclip.copy(translated)

