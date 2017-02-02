# Problem 2
# Fill in the class

class Cylinder(object):

    #class object attribute
    pi = 3.14

    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        # V = pi * r^2 * 2h

        vol = Cylinder.pi * (self.radius ** 2) * (self.height)

        return vol

    def surface_area(self):
        # A = (2 * pi * r * h)+(2 * pi * r^2)
        area = (2 * Cylinder.pi * self.radius * self.height) + (2 * Cylinder.pi * ( self.radius ** 2))
        return area


# EXAMPLE OUTPUT
c = Cylinder(2,3)
c.volume() #56.52
c.surface_area() #94.2
