def getIndexToIns(arrList, num):

    '''
        Assignment:

            Return the lowest index at which a value (second argument) should be inserted into an list (first argument) once it has been sorted. The returned value should be a number.

            For example, getIndexToIns([1,2,3,4], 1.5) should return 1 because it is greater than 1 (index 0), but less than 2 (index 1).

            Likewise, getIndexToIns([20,3,5], 19) should return 2 because once the list has been sorted it will look like [3,5,20] and 19 is less than 20 (index 2) and greater than 5 (index 1).

    '''

    arrList.append(num)                     # add the num arg to the list
    sortedList = sorted(arrList)            # sort it
    return sortedList.index(num)            # return the index of the num arg


getIndexToIns([40, 60], 50);
