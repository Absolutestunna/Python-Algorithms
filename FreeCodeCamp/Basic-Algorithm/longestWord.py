def findLongestWord(str):

    '''
        Assignment:

            Return the length of the longest word in the provided sentence.

            Your response should be a number.
    '''

    strLength = 0;

    for i in str.split():
        if len(i) > strLength:
            strLength = len(i)


    return strLength

findLongestWord("The dog at my flabargasted homework")
