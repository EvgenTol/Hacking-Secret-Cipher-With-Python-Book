'''
Book: Hacking Secret Ciphers with Python, by Al Sweigart
Author: Evgen Tolstykh

Page: 152
Chapter: 11

'''

import time , os , sys , Exercise_Chapter8_SetA , Exercise_Chapter9_SetA

def main():
    inputFile = "Test.encrypted.txt"
    outputFile = "Test.decrypted.txt"
    myKey = 10
    myMode = "decrypt"

    # if the input path is not correct, the programm terminates
    if not os.path.exists(inputFile):
        print("The file %s does not exist. Quitting..." % (inputFile))
        sys.exit()

    # if the the ouput file already exists, give the user a chance to quit
    if os.path.exists((outputFile)):
        print("This will override the file %s. (C)ontiniue or (Q)uit?" %(outputFile))
        response = input("> ")
        if not response.lower().startswith("c"):
            sys.exit()

    # read in the message from the input file
    fileObj = open(inputFile)
    content = fileObj.read()
    fileObj.close()

    print("%sing..." %(myMode.title()))

    # Measure how long the encryption/decryption takes

    startTime = time.time()
    if myMode == "encrypt":
        translated  = Exercise_Chapter8_SetA.encryptMessage(myKey , content)
    elif myMode == "decrypt":
        translated = Exercise_Chapter9_SetA.decryptMessage(myKey , content)
    totalTime = round(time.time() - startTime, 2)
    print("%sion time: %s seconds" %(myMode.title() , totalTime))

    # Write out the translated message to the output file
    outputFileObj = open(outputFile , "w")
    outputFileObj.write(translated)
    outputFileObj.close()

    print("Done %sing %s (%s characters)." %(myMode.title() , outputFile , len(content)))


if __name__ == "__main__":
    main()

'''

Page: 163
Set: A


1) Which is correct: os.exists() or os.path.exists()

1) => os.path.exists()

2) When is the UNIX epoch?

2) => 1.1.1970

What do the following expressions evaluate to?

1) 'Foobar'.startswith('Foo')

1) => True

2) 'Foo'.startswith('Foobar')

2) => False

3) 'Foobar'.startswith('foo')

3) => False

4) => 'bar'.endswith('Foobar')

4) => False

5) 'Foobar'.endswith('bar')

5) => True

6) 'The quick brown fox jumped over the yellow lazy dog.'.title()

6) => "The Quick Brown Fox Jumped Over The Yellow Lazy Dog."


'''