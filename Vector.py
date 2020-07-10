class Vector(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y)
    def __sub__(self,other):
        return Vector(self.x-other.x,self.y-other)
    def __mul__(self,s):
        return Vector(self.x*s,self.y*s)
    def __div__(self,s):
        float_s = float(s)
        return Vector(self.x/s,self.y/s)
    def __floordiv__(self, s):
        return Vector(self.x // s, self.y // s) 
    def __repr__(self):
        return 'Vector<{},{}>'.format(self.x,self.y)
a = Vector(3,4)
b = Vector(4,5)
c = a+b
d = 2
c = a//d
print(c)
