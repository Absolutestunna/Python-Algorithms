# Problem 3
# Write a function that asks for an integer and prints the square of it. Use a while loop with a try,except, else block to account for incorrect inputs.

def ask():

    while True:
        try:
            n = input('Input an integer: ')
        except:
            print('An error occurred! Please try again!')
            continue
        else:
            break


    print('Thank you, you number squared is: ', n**2)


ask()
# Input an integer: null
# An error occurred! Please try again!
# Input an integer: 2
# Thank you, you number squared is:  4
