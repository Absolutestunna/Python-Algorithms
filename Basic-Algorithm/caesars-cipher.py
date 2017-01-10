def rot13(str):

    '''
        Assignment:

            https://www.freecodecamp.com/challenges/caesars-cipher

            One of the simplest and most widely known ciphers is a Caesar cipher, also known as a shift cipher. In a shift cipher the meanings of the letters are shifted by some set amount.

            A common modern use is the ROT13 cipher, where the values of the letters are shifted by 13 places. Thus 'A' ↔ 'N', 'B' ↔ 'O' and so on.

            Write a function which takes a ROT13 encoded string as input and returns a decoded string.

            All letters will be uppercase. Do not transform any non-alphabetic character (i.e. spaces, punctuation), but do pass them on.

    '''

    finalStr = list()

    for char in str:
        if ord(char) >= 65 and ord(char) <= 77:
            finalStr.append(chr(ord(char) + 13))
        elif ord(char) >= 78 and ord(char) <= 90:
            finalStr.append(chr(ord(char) - 13))
        else:
            finalStr.append(char)

    return ' '.join(finalStr)

#Change the inputs below to test
rot13("SERR PBQR PNZC");
