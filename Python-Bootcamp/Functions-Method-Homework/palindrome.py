
def palindrome(s):
    '''
        Write a Python function that checks whether a passed string is palindrome or not.

        Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.

    '''

    return s == (s[::-1])


palindrome('helleh')
