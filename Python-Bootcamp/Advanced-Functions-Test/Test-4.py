def concatenate(L1, L2, connector):
    '''
        Use zip and list comprehension to return a list of the
        same length where each value is the two strings
        from L1 and L2 concatenated together with connector
        between them.
    '''

    zipped_tuple = list(zip(L1, L2))
    z2 = ['-'.join(result) for result in zipped_tuple]
    return z2



concatenate(['A','B'],['a','b'],'-') #['A-a', 'B-b']
