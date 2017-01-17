def destroyer(fargs, *args):

    '''
        Assignment:

            https://www.freecodecamp.com/challenges/seek-and-destroy

            You will be provided with an initial array (the first argument in the destroyer function), followed by one or more arguments. Remove all elements from the initial array that are of the same value as these arguments.

            Special note:

                'The special syntax, *args and **kwargs in function definitions is used to pass a variable number of arguments to a function. The single asterisk form (*args) is used to pass a non-keyworded, variable-length argument list, and the double asterisk form is used to pass a keyworded, variable-length argument list. Here is an example of how to use the non-keyworded form. This example passes one formal (positional) argument, and two more variable length arguments.'

                source: http://www.saltycrane.com/blog/2008/01/how-to-use-args-and-kwargs-in-python/

    '''

    return [x for x in fargs if x not in args]


destroyer([1, 2, 3, 1, 2, 3], 2, 3);
