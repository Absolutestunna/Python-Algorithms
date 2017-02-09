def word_lengths(phrase):

    '''
        Use map to create a function which finds the length of each word in the phrase (broken by spaces) and return the values in a list.

        The function will have an input of a string, and output a list of integers.

    '''
    return list(map(len, phrase.split( )))

word_lengths('How long are the words in this phrase') # output = [3, 4, 3, 3, 5, 2, 4, 6]
