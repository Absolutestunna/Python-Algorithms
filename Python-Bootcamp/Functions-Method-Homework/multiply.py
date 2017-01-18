from functools import reduce

def multiply(numbers):
    '''
        Write a Python function to multiply all the numbers in a list.

        Sample List : [1, 2, 3, -4]
        Expected Output : -24
    '''
    return reduce(lambda x, y: x * y, numbers)

multiply([1,2,3,-4])
