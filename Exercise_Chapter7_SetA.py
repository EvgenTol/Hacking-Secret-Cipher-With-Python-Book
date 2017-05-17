'''
Book: Hacking Secret Ciphers with Python, by Al Sweigart
Author: Evgen Tolstykh

Page: 94
Chapter: 7
Set: A
'''

# Caeser Cipher Hacker

message = "ZFBI. J'N QSFUUZ TVSF NZ DBU XPVME FBU NF." # the encrypted Message

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # all possible letters

# loop through every possible key
for key in range(len(LETTERS)):

    translated = ""

    #run the encryption/decryption code on each symbol in the message
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol) # get the number of the symbol
            num = num - key

            # handle the wrap-around if num is 26 or larger or less then 0
            if num < 0:
                num = num +len(LETTERS)

            # add numbers symbol at the end of translated
            translated = translated + LETTERS[num]

        else:
            # just add the symbol without encyption/decryption
            translated = translated + symbol


    print("Key #%s: %s" % (key, translated))


'''
Break the following ciphertexts:

1) R UXEN VH TRCCH,

1) => Key = 9

2) FR DBMMR EHOXL FX,
 
2) => Key = 19

3) CXPNCQNA FN'AN BX QJYYH,

3) => Key = 9

4) OBR OZKOMG QOFSTFSS.

4) => Key = 14

5) PDKQCD IU DAWZ DWO OQOLEYEKJO,

5) => Key = 22

6) FTMF U WQQB GZPQD YK TMF,

6) => Key = 12

7) AR ITMF YUSTF TMBBQZ,

7) => Key = Key = 12

8) DA D NCMVIF OJ OCZ NDUZ JA V MVO.

8) => Key = 21

9) ZFBI. J'N QSFUUZ TVSF NZ DBU XPVME FBU NF.

9) => Key = 1 
'''