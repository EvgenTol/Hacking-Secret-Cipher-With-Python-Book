'''
Book: Hacking Secret Ciphers with Python, by Al Sweigart
Author: Evgen Tolstykh

Page: 97
Chapter: 8

'''

# Transposition Cipher Decryption

import math

def main():

    myMessage = "Cenoonommstmme oo snnio. s s c"
    myKey = 8

    plaintext = decryptMessage(myKey , myMessage)

    print(plaintext + "|")

def decryptMessage(key , message):

    # the Number of "columns" in our transposition grid:
    numOfColumns = math.ceil(len(message) / key)
    # the Number of "rows" in our grid
    numOfRows = key
    # The number of "shaded boxes" in the last "column" of the grid
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

    # Each string in Plaintext represents a column in the grid
    plaintext = [""] * numOfColumns

    # The col na drow variables point to were in the grid the next characters in the set encrypted message will go
    col = 0
    row = 0

    for symbol in message:
        plaintext[col] += symbol
        col += 1 # point to next column

        # if there are no more columns OR we're at a shaded box, go back to the first  column and the nexr row
        if(col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            col = 0
            row += 1

    return "".join(plaintext)

if __name__ == "__main__":
    main()

'''

Page: 131
Set: B

If you enter the following pieces of code into the interactive shell, what does it print out?

1) math.ceil(3.1)

1) => 4

2) math.ceil(3.0)
 
2) => 3

3) math.floor(3.1)

3) => 3

4) math.floor(3.0)

4) => 3

5) round(3.1)

5) => 5

6) round(3.0)

6) => 6

7) round(3.5)

7) => 4

8) True and True

8) => True

9) True and False

9) => False

10) False and True

10) => False

11) False and False

11) => False

12) True or True

12) => True

13) True or False

13) => True

14) False or True

14) => True

15) False or False

15) => False

16) not True

16) => False

17) not not True

17) => True


Page: 135
Set: C

Draw out the complete truth tables for the and, or, and not operators.

and:

A   B   or  and
1   1   1   1
1   0   1   0
0   1   1   0   
0   0   0   0

A   not
1   0
0   1

Which is correct?

1) if __name__ == '__main__':
    
1) => correct

2) if __main__ == '__name__':

2) => not correct

3) if _name_ == '_main_':

3) => not correct

4) if _main_ == '_name_':

4) => not correct


'''