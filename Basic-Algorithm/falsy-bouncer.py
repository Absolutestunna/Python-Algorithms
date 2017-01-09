def bouncer(arrList):

    '''
        Assignment:
            https://www.freecodecamp.com/challenges/falsy-bouncer

            Remove all falsy values from an array.

            Falsy values in JavaScript are false, null, 0, "", undefined, and NaN.
    '''

    filter(lambda x: return bool(x) != False, arrList)


bouncer([7, "ate", "", false, 9]);
