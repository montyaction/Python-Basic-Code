# class variable
# circle
# area
# circum
class Circle:
    def __init__(self, radius, pi):
        self.radius = radius
        self.pi = pi
    def calc_circumference(self):
        return 2*self.pi*self.radius

c = Circle(4, 3.14)
c1 = Circle(5, 3.14)
print(c.calc_circumference())

#-----------not_repeat_method---------

class Circle2:
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius
    def calc_circumference(self):
        return 2*Circle2.pi*self.radius

c2 = Circle2(4)
c3 = Circle2(5)
print(c2.calc_circumference())