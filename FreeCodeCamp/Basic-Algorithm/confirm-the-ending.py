def confirmEnding(str, target):

    '''
        Assignment:
        
            https://www.freecodecamp.com/challenges/confirm-the-ending
            Check True if a string (first argument, str) ends with the given target string (second argument, target).

    '''

    split_str = str.split();               #get a new list

    if len(split_str) > 1:                 # check if the list is > 1
        last_word = split_str.pop()        # get the last word
        return last_word == target         # return a bool after evaluation
    else:
        i_value = str[len(str) - 1]        # get the last word
        return i_value == target           # return a bool after evaluation

confirmEnding("Walking", "f")                 #should return False

confirmEnding("Walking in the rain", "rain")  #should return True
