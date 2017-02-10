

def d_list(L):
    '''
        Use enumerate and other skills to return a dictionary which has the values of the list as keys and the index as the value. You may assume that a value will only appear once in the given list.
    '''
    #Solution 1
    # dict_answer = {}
    # for counter, key in enumerate(L):
    #     dict_answer[key] = counter
    #
    # return dict_answer

    #Solution 2
    [{counter: key} for counter,key in enumerate(L)]


d_list(['a','b','c']) #{'a': 0, 'b': 1, 'c': 2}
