
def up_low(str):

    '''
        Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

        Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
        Expected Output :
        No. of Upper case characters : 4
        No. of Lower case Characters : 33

        If you feel ambitious, explore the Collections module to solve this problem!

    '''

    upper_count = 0
    lower_count = 0

    answer_string = "No. of Upper case characters : {} \n No. of Lower case Characters : {}"

    for x in list(str):
        if x.istitle():
            upper_count += 1
        elif x.islower():
            lower_count += 1

    return answer_string.format(upper_count, lower_count)

up_low('Hello Mr. Rogers, how are you this fine Tuesday?')
