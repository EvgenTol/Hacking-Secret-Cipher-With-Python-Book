'''
Book: Hacking Secret Ciphers with Python, by Al Sweigart
Author: Evgen Tolstykh

Page: 196
Chapter: 14


What do the following expressions evaluate to?

1) 11 % 5

1) => 1

2) 21 % 7

2) => 0

3) 17 % 1000

3) => 17

4) 5 % 5

4) => 0

5) Is 4 a factor of 8?

5) => yes

6) Is 4 a factor of 10?

6) => No

7) Is 4 a factor of 12?

7) => Yes

8) What is the greatest common factor of 10 and 15?

8) => 5

9) What is the greatest common factor of 6 and 8?

9) => 2
'''

def gcd(a, b):
    while a != 0:
        a ,b = b % a, a
    return b

'''

Page: 202
Set: C

1) What does spam contain after executing spam, eggs = 'hello', 'world'?

1) => "hello"

2) The greatest common factor of 17 and 31 is 1. Are 17 and 31 relatively prime?

2) => yes

3) Why aren't 6 and 8 relatively prime?

3) => because gcd is 2 => gcd != 1

4) If two numbers are realtively prime, are they also coprime?

4) => yes

5) What's the difference between a divisor and a factor?

5) => 

6) Write out the code for the Python function that calculates greatest common divisor.

6) =>
def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b

7) Write it out again, just to help yourself memorize it.

7) =>
def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b


Page: 204
Set: D

1) In the shift cipher, the symbol's number is added to the key's number. What is done in the multiplicative cipher?

1) => it is multiplied
'''

def findModInverse(a, m):
    if gcd(a, m) != 1:
        return None # no mod inverse exists if a & m arent relativley prime
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1),
