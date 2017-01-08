def confirmEnding(str, target):

    '''
        Assignment:

            https://www.freecodecamp.com/challenges/confirm-the-ending

            Check if a string (first argument, str) ends with the given target string (second argument, target).

        Special notes:
            in is used to check if target argument is a substring of str argument

    '''

    return target in str




confirmEnding("Walking on water and developing software from a specification are easy if both are frozen", "specification")

confirmEnding("Walking", "g")
