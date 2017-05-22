'''
Book: Hacking Secret Ciphers with Python, by Al Sweigart
Author: Evgen Tolstykh

Page: 137
Chapter: 10

'''

import random, sys , Exercise_Chapter9_SetA , Exercise_Chapter8_SetA

def main():

    random.seed(42)

    for i in range(20): # run 20 tests
        # Generate random messages to test

        # the message will have a random length

        message = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * random.randint(4 , 40)

        # Convert the message string to a list to shuffle it
        message = list(message)
        random.shuffle(message)

        message = "".join(message) # convert list to string

        print('Test #%s: "%s..."' % (i+1, message[:50]))

        #check all possible keys for each message
        for key in range(1 , len(message)):
            encrypted = Exercise_Chapter8_SetA.encryptMessage(key , message)
            decrypted = Exercise_Chapter9_SetA.decryptMessage(key , encrypted)

            # if the decryption doesnt match the original message, display an error message and quit
            if message != decrypted:
                print("Mismatch with key %s and message %s." % (key , message))
                print(decrypted)
                sys.exit()


    print("Transposition cipher test passed")


if __name__ == "__main__":
    main()

'''
Page: 146
Set: A


1) If you ran this program and it printed the number 7, what would it print the next time you run it?


import random
random.seed(9)
print(random.randint(1, 10))

1) => 7

2) What does this program print out?

spam = [1, 2, 3]
eggs = spam
ham = eggs
ham[0] = 99
print(ham == spam)

2) => True

3) What module contains the deepcopy() function?

3) => copy

4) 
What does this program print out?
import copy
spam = [1, 2, 3]
eggs = copy.deepcopy(spam)
ham = copy.deepcopy(eggs)
ham[0] = 99
print(ham == spam)

4) => False

'''