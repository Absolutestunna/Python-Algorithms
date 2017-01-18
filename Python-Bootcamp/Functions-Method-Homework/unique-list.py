
def unique_list(l):
    '''
        Write a Python function that takes a list and returns a new list with unique elements of the first list.

        Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
        Unique List : [1, 2, 3, 4, 5]
        In [13]:
    '''
    return set(l)

unique_list([1,1,1,1,2,2,3,3,3,3,4,5])
