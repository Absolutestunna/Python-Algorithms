def mutation(arrList):
    '''

        Assignment:

            Return true if the string in the first element of the list contains all of the letters of the string in the second element of the list.

            For example, ["hello", "Hello"], should return true because all of the letters in the second string are present in the first, ignoring case.

            The arguments ["hello", "hey"] should return false because the string "hello" does not contain a "y".

            Lastly, ["Alien", "line"], should return true because all of the letters in "line" are present in "Alien".

    '''

    for char in arrList[1]:
        if char not in arrList[0]:
            return False

    return True

mutation(["Alien", "line"])
