'''
Book: Hacking Secret Ciphers with Python, by Al Sweigart
Author: Evgen Tolstykh

Page: 67
Chapter: 5
Set: B

What do the following pieces of code display on the screen?

1) print(len('Hello') + len('Hello'))

1) => 10

2) 
i = 0
while i < 3:
    print('Hello')
    i = i + 1
    
2) => 
Hello
Hello
Hello

3) 
i = 0
spam = 'Hello'
while i < 10:
    spam = spam + spam[i]
    i = i + 1
print(spam)

3) => HelloHelloHello

4)
i = 0
while i < 4:
    while i < 6:
        i = i + 2
        print(i)

4) => 
2
4
6

'''