'''
Book: Hacking Secret Ciphers with Python, by Al Sweigart
Author: Evgen Tolstykh

Page: 97
Chapter: 8

'''

# Transposition Cipher Encryption

def main():

    myMessage = "Common sense is not so common" # Message to be encrypted
    myKey = 8 # Encryption key

    ciphertext = encryptMessage(myKey, myMessage)

    # Print the encrypted string in ciphertext to the screen, with a | after it in case there are spaces at the end
    # of the encrypted message
    print(ciphertext + "|")

def encryptMessage(key, message):
    # each String in ciphertext represents a column in the grid
    ciphertext = [""] * key

    # Loop through each Column in ciphertext
    for col in range(key):
        pointer = col

        # Keep looping until pointer goes past the length of the message
        while pointer < len(message):
            # Place the charcter at pointer in message at the end of the current column in the ciphertext list
            ciphertext[col] += message[pointer]

            # move pointer over
            pointer += key

    # Convert the cipertext list into a single string value and return it
    return "".join(ciphertext)

if __name__ == "__main__":
    main()

'''

Page: 105
Set: B

In the following programs, is spam a global or local variable? Or are there both a global and local variables named spam?

1) spam = 42

1) => global

2) 
def foo():
    spam = 42
    
2) => local

3) 
spam = 42
def foo():
    spam = 42

3) => both

4) 
spam = 42
def foo():
    print(spam)
    
4) => global

5) 
spam = 42
def foo():
    global spam
    print(spam)
    
5) => global

6) 
spam = 42
def foo():
    global spam
    spam = 99
    print(spam)
    
6) => global

7) 
spam = 42
def foo():
    spam = 99
    print(spam)
    
7) => both


Page: 109
Set: C

What value do each of the following expressions evaluate to?

1)  [0, 1, 2, 3, 4][2]

1) => 2

2) [1, 2, 3, 4][2]

2) => 3

3) [[1, 2], [3, 4]][0]

3) => [1 , 2]

4) [[1, 2], [3, 4]][1]

4) => [3 , 4]

5) [[1, 2], [3, 4]][0][1]

5) => 2

6) [[1, 2], [3, 4]][1][1]

6) => 4

7) ['hello'][0]

7) => "hello"

8) ['hello'][0][1]

8) => "e"

9) [2, 4, 6, 8, 10][1:3]

9) => [4 , 6]

10) list('Hello world!')

10) => ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', '!']

11) list(range(10))

11) => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

12) list(range(10))[2]

12)= > 2

Page: 111
Set: D

What value do each of the following expressions evaluate to?

1) len([2, 4])

1) => 2

2) len([])

2) => 0

3) len(['', '', ''])

3) => 3

4) [4, 5, 6] + [1, 2, 3]

4) => [4 , 5 , 6 , 1 , 2 , 3]

5) 3 * [1, 2, 3] + [9]

5) => [1 , 2 , 3 , 1 , 2 , 3 , 1 , 2 , 3 , 9]

6) 42 in [1, 2, 3]

6) => False

7) 42 in [41, 42, 42, 42]

7) => True

Page: 117
Set: E

What are the four augmented assignment operators?

=> += , -= , /= , *=

What do the following pieces of code display on the screen?

1) 
spam = 'hello'
spam += 'world'
print(spam)

1) => helloworld

2) 
spam = 3
spam += 3
spam += 3
print(spam)

2) => 9

3) ''.join(['hello', 'world'])

3) => "helloworld"

4) ' '.join(['my', 'very', 'special', 'mudder'])

4) => "my very special mudder"
'''
