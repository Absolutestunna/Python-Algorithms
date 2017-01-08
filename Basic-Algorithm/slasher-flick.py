def slasher(arr, howMany):

    '''
        https://www.freecodecamp.com/challenges/slasher-flick

        Assignment:

            Return the remaining elements of an array after chopping off n elements from the head.

            The head means the beginning of the array, or the zeroth index.
    '''


    return arr[howMany:]

slasher([1, 2, 3], 2);
