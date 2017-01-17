import re

def titleCase(str):
    '''
        Assignment:

            Return the provided string with the first letter of each word capitalized. Make sure the rest of the word is in lower case.

            For the purpose of this exercise, you should also capitalize connecting words like "the" and "of".

            Answer was provided in the Python docs:

                https://docs.python.org/3/library/stdtypes.html#str.title

    '''

    return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
                 lambda mo: mo.group(0)[0].upper() + mo.group(0)[1:].lower(),
                 str)

titleCase("I'm a little tea pot");
