import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    '''
        Write a Python function to check whether a string is pangram or not.

        Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
        For example : "The quick brown fox jumps over the lazy dog"
        
    '''
    for letter in alphabet:
        if letter not in str1:
            return False
    else:
        return True


ispangram("The quick brown fox jumps over the lazy dog")
