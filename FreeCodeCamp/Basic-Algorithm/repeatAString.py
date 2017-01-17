def repeatStrNumTimes(str, num):

    '''
        Assignment:

            Repeat a given string (first argument) num times (second argument). Return an empty string if num is not a positive number.


    '''

    if num <= 0:
        return ""
    else:
        return str * num

repeatStrNumTimes('abc', 3)
