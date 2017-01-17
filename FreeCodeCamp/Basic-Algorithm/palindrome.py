import re

def palindrome(str):
    '''
        Assignment:

            A palindrome is a word or sentence that's spelled the same way both forward and backward, ignoring punctuation, case, and spacing.

            Note:
            You'll need to remove all non-alphanumeric characters (punctuation, spaces and symbols) and turn everything lower case in order to check for palindromes.

            We'll pass strings with varying formats, such as "racecar", "RaceCar", and "race CAR" among others.

            We'll also pass strings with special symbols, such as "2A3*3a2", "2A3 3a2", and "2_A3*3#A2".


        Special notes:
        re module provides regular expression matching operations similar to those found in Perl.

        https://docs.python.org/3.5/library/re.html


    '''

    finalStr = re.sub("[^a-zA-Z]", "", str) # re.sub(MATCH PATTERN, STRING REPLACEMENT, STRING TO SEARCH)

    return finalStr

palindrome('_eye')
