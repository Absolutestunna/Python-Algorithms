def chunkArrayInGroups(arr, size):

    '''
        Assignment:

            https://www.freecodecamp.com/challenges/chunky-monkey

            Write a function that splits an list (first argument) into groups the length of size (second argument) and returns them as a two-dimensional list.


    '''

    #solution 1
    listGroups = list()

    for i in range(0, size):
        listGroups.append(arr[0: size])
        del(arr[0: size])    #delete the sliced group after it's been saved. Not efficient. Need to                dynamically slice the arr on the appropriate indices.

    return listGroups



chunkArrayInGroups(["a", "b", "c", "d"], 2);