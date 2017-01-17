def mutation(arrList):
    '''

        Assignment:

            Return true if the string in the first element of the list contains all of the letters of the string in the second element of the list.

            For example, ["hello", "Hello"], should return true because all of the letters in the second string are present in the first, ignoring case.

            The arguments ["hello", "hey"] should return false because the string "hello" does not contain a "y".

            Lastly, ["Alien", "line"], should return true because all of the letters in "line" are present in "Alien".

        Special notes:

            ord: Given a string representing one Unicode character, return an integer representing the Unicode code point of that character. For example, ord('a') returns the integer 97 and ord('€') (Euro sign) returns 8364. This is the inverse of chr().

            chr: Return the string representing a character whose Unicode code point is the integer i. For example, chr(97) returns the string 'a', while chr(8364) returns the string '€'. This is the inverse of ord().

            The valid range for the argument is from 0 through 1,114,111 (0x10FFFF in base 16). ValueError will be raised if i is outside that range.

    '''

    for char in arrList[1]:
        if char not in arrList[0]:
            return False

    return True

mutation(["Alien", "line"])
