

def count_match_index(L):
    '''
        Use enumerate and other skills from above to return the count of the number of items in the list whose value equals its index.
    '''

    #Solution 1
    # logger = 0
    #
    # for counter, num in enumerate(L):
    #     if counter == num:
    #         logger+=1
    #
    # return logger

    #Solution2

    return len([key for counter, key in enumerate(L) if key == counter])




count_match_index([0,2,2,1,5,5,6,10]) #4
