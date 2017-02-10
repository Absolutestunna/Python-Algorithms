
def filter_words(word_list, letter):
    '''
        Use filter to return the words from a list of words which start with a target letter.

    '''

    #Solution 1
    # def filter_words(word):
    #     if word[0] == letter:
    #         return word
    #
    # return list(filter(filter_words, l)

    #Solution 2
    return list(filter(lambda word: word[0]==letter, word_list))

l = ['hello','are','cat','dog','ham','hi','go','to','heart']
filter_words(l,'h')  #['hello', 'ham', 'hi', 'heart']
