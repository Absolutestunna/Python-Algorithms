def factorialize(int):
    if (int <= 0):
        return 1
    return int * factorialize(int - 1)

factorialize(5)
