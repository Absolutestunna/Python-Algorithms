# Problem 2
# Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done.'


try:
    x = 5
    y = 0

    z = x/y
except:
    print('cannot divide by zero')
finally:
    print('All done')

# ---------------------------------------------------------------------------
# ZeroDivisionError                         Traceback (most recent call last)
# <ipython-input-2-3effb78be709> in <module>()
#       2 y = 0
#       3
# ----> 4 z = x/y
#
# ZeroDivisionError: integer division or modulo by zero
