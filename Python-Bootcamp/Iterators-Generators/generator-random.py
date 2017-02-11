import random


def rand_num(low,high,n):
    for i in range(n):
        yield random.randint(low,high)

for num in rand_num(1,10,12):
    print num

# 6
# 7
# 6
# 9
# 9
# 4
# 3
# 7
# 8
# 1
# 6
# 1
