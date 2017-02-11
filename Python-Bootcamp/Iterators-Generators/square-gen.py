def gensquares(N):
    '''

        Create a generator that generates the squares of numbers up to some number N.

    '''
    for i in range(N):
        yield i ** 2

for x in gensquares(10):
    print x


# 0
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81
