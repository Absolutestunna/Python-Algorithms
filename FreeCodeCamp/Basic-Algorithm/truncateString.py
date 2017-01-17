def truncateString(str, num):
    '''
        Assingment:

            https://www.freecodecamp.com/challenges/truncate-a-string

            Truncate a string (first argument) if it is longer than the given maximum string length (second argument). Return the truncated string with a ... ending.

            Note that inserting the three dots to the end will add to the string length.

            However, if the given maximum string length num is less than or equal to 3, then the addition of the three dots does not add to the string length in determining the truncated string.
    '''

    updatedString = []

    if num < 3:
        updatedString = str[0:num] + "..."
    elif len(str) == num:
        updatedString = str
    else:
        updatedString = str[0: num-3] + "..."

    return updatedString

truncateString("A-tisket a-tasket A green and yellow basket", 11);
