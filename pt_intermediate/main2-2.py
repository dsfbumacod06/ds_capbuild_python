#overloading

class Vector:
    def __init__(self,x,y):
        self.x = x 
        self.y = y

    def __add__ (self, otherVector):
        return Vector(self.x + otherVector.x, self.y + otherVector.y)
    def __sub__ (self, otherVector):
        return Vector(self.x - otherVector.x, self.y - otherVector.y)
    def __str__(self):
        return str({f"X": self.x,"Y":self.y})
    

vector1 = Vector(2,5)
vector2 = Vector(6,3)

print(vector1)
print(vector2)

vector3 = vector1 + vector2

print(vector3)

vector4 = vector1 - vector2

print(vector4)