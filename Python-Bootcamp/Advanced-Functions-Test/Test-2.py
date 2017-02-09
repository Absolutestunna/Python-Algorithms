
def digits_to_num(digits):
    '''
        Use reduce to take a list of digits and return the number that they correspond to. Do not convert the integers to strings!

    '''
    reduce(lambda x: x, digits)

digits_to_num([3,4,3,2,1]) #output 34321
