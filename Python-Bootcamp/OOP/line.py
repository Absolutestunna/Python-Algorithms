# Problem 1
# Fill in the Line class methods to accept coordinate as a pair of tuples and return the slope and distance of the line.

class Line(object):

    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        
        #distance formulae = ((x2 - x1)^2 + (y2 - xy)^2) ** (1/2)
        first_square = (self.coor2[0] - self.coor1[0]) ** 2
        second_square = (self.coor2[1] - self.coor1[1]) ** 2

        dist =  ( first_square + second_square ) ** (1/2)
        return dist

    def slope(self):

        #slope = (y2 - y1) / (x2 - x1)
        slope_val = ( (self.coor2[1] - self.coor1[1])  / (self.coor2[0] - self.coor1[0]) )
        return slope_val

# EXAMPLE OUTPUT

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
li.distance()   #9.433981132056603
li.slope()      #1.6
