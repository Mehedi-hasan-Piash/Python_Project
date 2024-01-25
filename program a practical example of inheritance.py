class Shape :
    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    def area (self) :
        print("i am area method of shape class")

class Triangle(Shape) :
    def area(self):
        area = 0.5 * self.dim1 * self.dim2
        print("Area of Triangle : ", area)

class Rectangle(Shape) :
    def area(self):
        area = self.dim1 * self.dim2
        print("Area of Rectangle : ", area)

tl = Triangle(10, 20)
tl.area()

rl = Rectangle(20, 30)
rl.area()





