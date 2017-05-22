'''
Book: Hacking Secret Ciphers with Python, by Al Sweigart
Author: Evgen Tolstykh

Page: 167
Chapter: 12

'''

# For this Programm to work, there needs to be a dictionary.txt file in this directory
# to use:
# import Exercise_Chapter12_SetA
# Exercise_Chapter12_SetA.isEnglish(STRING)  >= return True or False

UPPERLETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + " \t\n"

def loadDictionary():
    dictionaryFile = open("dictionary.txt")
    englishWords = {}
    for word in dictionaryFile.read().split("\n"):
        englishWords[word] = None
    dictionaryFile.close()
    return englishWords

ENGLISH_WORDS = loadDictionary()

def getEnglishCount(message):
    message = message.upper()
    message = removeNonLetters(message)
    possibleWords = message.split()

    if possibleWords == []:
        return 0.0

    matches = 0
    for word in possibleWords:
        if word in ENGLISH_WORDS:
            matches +=1
    return float(matches) / len(possibleWords)

def removeNonLetters(message):
    lettersOnly = []
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            lettersOnly.append(symbol)
    return "".join(lettersOnly)

def isEnglish(message , wordPercentage = 20 , letterPercentage = 85):
    # By default 20% Words must exist in the Dictionary and 85% of all the characters in the message must be letters and spaces
    wordsMatch = getEnglishCount(message) * 100 >= wordPercentage
    numLetters = len(removeNonLetters(message))
    messageLettersPercentage = float(numLetters) / len(message) * 100
    lettersMatch = messageLettersPercentage >= letterPercentage
    return wordsMatch and lettersMatch


'''

Page: 171
Set: A

1) What is a Python dictionary?

1) =>  A data type of values that can store multiple values like a list, except they can use any value for their index.

2) Python lists use square brackets [ and ] to type them out. What do dictionaries use?

2) => { and }

3) 
What does the following code print?
>>> spam = {'name': 'Al'}
>>> spam['name']
>>> print(spam['name'])

3) => Al

Page: 172
Set: C

1) What does this code print?
>>> spam = {'eggs': 'bacon'}
>>> print(len(spam))

1) => 1

2) What does this code print?
>>> spam = {'eggs': 'bacon'}
>>> print('eggs' in spam)

2) => True

3) What does this code print?
>>> spam = {'eggs': 'bacon'}
>>> print('bacon' in spam)

3) => False

4) What for loop code would print out the values in the following spam dictionary?
>>> spam = {'name': 'Zophie', 'species':'cat', 'age':8}

4) => 
for i in spam:
    print(spam[i])
    
    
Page: 178
Set: D

1) What are three differences between dictionaries and lists?

1) => 
Dictionary key-value pairs are not in any order.
Dictionaries cannot be concatenated with the + operator.
Lists have integer indexes, but dictionary keys can be of any data type.

2) What does the following print?
>>> print('Hello, world!'.split())

2) => ["Hello" , "world"]

3) What is the None value?

3) => The lack of a value

4) How many different values does the NoneType data type have?

4) => 1 , None

5) What happens if your code attempts to divide by zero?

5) => Error, DivideByZero

Page: 182
Set: E

1) Where does the append() method add values to a list?

1) => end of the List

2) What is a default argument?

2) => if no paramters are give, the function takes the default argument as paramter

3) What will the following print?
def spam(eggs=42):     print(eggs)
spam()
spam('Hello')

3) => 
42
Hello

4) 
What percentage of words in this sentence are valid English words?
"Whether it's flobulllar in the mind to quarfalog the slings and arrows out outrageous guuuuuuuuur."

4) => Total Words = 15 , English Words = 12 , Percentage = > 12/15 * 100 => 80
'''

