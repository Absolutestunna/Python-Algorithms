def bouncer(arrList):

    '''
        Assignment:
            https://www.freecodecamp.com/challenges/falsy-bouncer

            Remove all falsy values from an array.

            Falsy values in JavaScript are false, null, 0, "", undefined, and NaN.

        Special Notes: List Comprehension's construction starts with an expression, a for in statement, n number of 'for in' and 'if' statements
    '''

    return [x for x in arrList if bool(x) != False]


bouncer([7, "ate", "", false, 9]);
