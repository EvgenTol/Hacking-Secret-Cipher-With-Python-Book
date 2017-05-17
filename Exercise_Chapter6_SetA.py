'''
Book: Hacking Secret Ciphers with Python, by Al Sweigart
Author: Evgen Tolstykh

Page: 72
Chapter: 6
Set: A

'''

#import pyperclip

#String to be encrypted/decrypted
message = "Xqp whh ahoa kb pda sknhz swo ejreoexha."

#Key for encryption/decryption
key = 22

# Tells the programm to encrypt or decrypt
mode = "decrypt"

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

'''
Using the cipher program, encrypt the following sentences with the given keys:

1) “'You can show black is white by argument,' said Filby, 'but you will never convince me.'” with the key 8.
2) “1234567890” with key 21.

1) => 'GWC KIV APWE JTIKS QA EPQBM JG IZOCUMVB,' AIQL NQTJG, 'JCB GWC EQTT VMDMZ KWVDQVKM UM.'
2) => 1234567890

Using the cipher program, decrypt the following ciphertexts with the given keys:

1) “'Kv uqwpfu rncwukdng gpqwij.'” with key 2.
2) “Xqp whh ahoa kb pda sknhz swo ejreoexha.” with key 22.

1) => 'IT SOUNDS PLAUSIBLE ENOUGH.'
2) => BUT ALL ELSE OF THE WORLD WAS INVISIBLE.

Using the cipher program, encrypt the following sentence with the key 0:

1) This is still a silly example.”

1) => This is still a silly example.”

Set: B
Page: 77

What Python instruction would import a module named watermelon.py?

=> import watermelon

The variable SPAM is a constant. Will this code cause an error?: SPAM = 'hello'

=> no

What do the following pieces of code display on the screen?

1) 
for i in 'hello':
    print(i)

1) => 
h
e
l
l
o

2) print('Hello'.lower())

2) => "hello"

3) print('Hello'.upper())

3) => "HELLO"

4) print('Hello'.upper().lower().upper().lower())

4) => "hello"

BONUS: What does this program display on the screen? (Guess, and then type it in and run it to find out.)

5) 
spam = 'foo'
for i in spam:
    spam += i
print(spam)

5) => foofoo



Set: C
Page: 81

What do the following pieces of code display on the screen?

1) 
if 10 < 5:
    print('Hello')
    
1) => nothing

2) 
if 10 < 5:
    print('Hello')
else:
    print('Goodbye')
    
2) => Goodbye

3) 
if 10 < 5:
    print('Hello')
elif 5 == 5:
    print('Alice')
else:
    print('Goodbye')
    
3) => Alice

4) 
if 10 < 5:
    print('Hello')
elif False:
    print('Alice')
else:
    print('Goodbye')
    
4) => Goodbye

5) 
if 10 < 5:
    print('Hello')
elif False:
    print('Alice')
elif 5 != 5:
    print('Bob')
else:
    print('Goodbye')
    
5) => Goodbye

6) 
if 10 < 5:
    print('Hello')
elif 5 == 5:
    print('Alice')
else:
    print('Goodbye')
    
6) => Alice

7)
if 10 < 5:
    print('Hello')
else:
    print('Goodbye')
elif 5 == 5:
    print('Alice')
    
7) => error

8) print('f' in 'foo')

8) => True

9) print('f' not in 'foo')

9) => False

10) print('foo' in 'f')

10) => False

11) print('hello'.find('o'))

11) => 4

12) print('hello'.find('oo'))

12) => -1
'''