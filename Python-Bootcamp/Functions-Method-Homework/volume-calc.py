# Functions and Methods Homework

import math

def vol(rad):
    '''

      Write a function that computes the volume of a sphere given its radius.

      Volume definition:
      http://www.aaamath.com/exp79_x8.htm

      volume = 4/3 π r3


    '''

    volume = (4/3) * math.pi * (rad ** 3)
    return volume

vol(3)
