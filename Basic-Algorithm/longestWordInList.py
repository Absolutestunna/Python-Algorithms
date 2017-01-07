def findLongestWord(lis):

    '''
        Assignment:

            https://www.freecodecamp.com/challenges/return-largest-numbers-in-list

            Return a list (an array) consisting of the largest number from each provided sub-list (sub-array). For simplicity, the provided list will contain exactly 4 sub-lists.

            Remember, you can iterate through an list with a simple for loop, and access each member with array syntax arr[i].

    '''

    #Solution 1
    # finalArr, evaluator = [], 0
        
    # for x in lis:
    #     for y in x:
    #         if y > evaluator:
    #             evaluator = y
    #
    #     finalArr.append(evaluator)
    #

    # return finalArr

    #Solution 2

    [evaluate(y) x in lis y in x]

    def evaluate(y):
        if y > evaluator:
            evaluator = y

largestOfFour([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]);
