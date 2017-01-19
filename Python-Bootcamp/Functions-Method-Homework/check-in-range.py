
def ran_bool(num,low,high):

    '''
        Write a function that checks whether a number is in a given range (Inclusive of high and low)
    '''
    return num in (range(low, high + 1))  #add 1 to include the range in the test

ran_bool(3,1,10)
