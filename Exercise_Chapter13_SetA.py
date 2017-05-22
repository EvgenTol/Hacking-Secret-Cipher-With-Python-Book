'''
Book: Hacking Secret Ciphers with Python, by Al Sweigart
Author: Evgen Tolstykh

Page: 183
Chapter: 13

'''

import Exercise_Chapter12_SetA , Exercise_Chapter9_SetA

def main():
    myMessage = """Cb b rssti aieih rooaopbrtnsceee er es no npfgcwu  plri ch nitaalr eiuengiteehb(e1  hilincegeoamn fubehgtarndcstudmd nM eu eacBoltaeteeoinebcdkyremdteghn.aa2r81a condari fmps" tad   l t oisn sit u1rnd stara nvhn fsedbh ee,n  e necrg6  8nmisv l nc muiftegiitm tutmg cm shSs9fcie ebintcaets h  aihda cctrhe ele 1O7 aaoem waoaatdahretnhechaopnooeapece9etfncdbgsoeb uuteitgna.rteoh add e,D7c1Etnpneehtn beete" evecoal lsfmcrl iu1cifgo ai. sl1rchdnheev sh meBd ies e9t)nh,htcnoecplrrh ,ide hmtlme. pheaLem,toeinfgn t e9yce da' eN eMp a ffn Fc1o ge eohg dere.eec s nfap yox hla yon. lnrnsreaBoa t,e eitsw il ulpbdofgBRe bwlmprraio po  droB wtinue r Pieno nc ayieeto'lulcih sfnc  ownaSserbereiaSm-eaiah, nnrttgcC  maciiritvledastinideI  nn rms iehn tsigaBmuoetcetias rn"""

    hackedMessage = hackTransposition(myMessage)

    if hackedMessage == None:
        print("Failes to hack the encryption")
    else:
        print("Copying hacked message")
        print(hackedMessage)


def hackTransposition(message):
    print("hacking...")
    print("(Press Ctrl-C or Ctrl-D to quit at any time)")

    # brute-force by looping through every possible Key
    for key in range(1 , len(message)):
        print("Trying key #%s..." %(key))

        decryptText = Exercise_Chapter9_SetA.decryptMessage(key , message)

        if Exercise_Chapter12_SetA.isEnglish(decryptText):
            # Check with user to see if the decrypted has been found
            print()
            print("possible encryption hack:")
            print("Key %s: %s" %(key , decryptText[:100]))
            print()
            print("Enter D for done, or just press Enter to continiue hacking:")
            response = input("> ")
            if response.strip().upper().startswith("D"):
                return decryptText

    return None

if __name__ == "__main__":
    main()


'''

Page: 192
Set: A

1) What does this expression evaluate to: ' Hello world'.strip()

1) => "Hello world"

2) Which characters are whitespace characters?

2) => The space, newline, and tab characters.

3) Why does 'Hello world'.strip('o') evaluate to a string that still has o's in it?

3) => The o's are not at the beginning or end of the string.

4) Why does 'xxxHelloxxx'.strip('X') evaluate to a string that still has x's in it?

4) =>  there are no uppercase X's

'''