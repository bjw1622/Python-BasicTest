"""first = int(input("시작 수를 입력하세요:"))
end = int(input("끝 수를 입력하세요:"))
print("-"*30)

sum =0
for i in range(first,end+1):
    if(i % 5 != 0 ):
        sum = sum + i

print(f"100에서 200까지 5의 배수가 아닌 수의 합계: {sum}")
"""

# 2017210005 조민규
# 실습#4
from abc import *


class Shape(metaclass=ABCMeta):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def getArea(self):
        pass


class Circle(Shape):
    phi = 3.14

    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def getArea(self):
        return Circle.phi * (self.radius * self.radius)
        # overriding

    def __str__(self):
        return f"Circle({self.color},{self.radius}) 면적 =  {self.getArea()}"


class Rectangle(Shape):
    def __init__(self, color, length, breadth):
        super().__init__(color)
        self.length = length
        self.breadth = breadth

    def getArea(self):
        return self.length * self.breadth
        # overriding

    def __str__(self):
        return f"Rectangle({self.color},{self.length},{self.breadth}) 면적 =  {self.getArea()}"


class Triangle(Shape):
    def __init__(self, color, base, height):
        super().__init__(color)
        self.base = base
        self.height = height

    def getArea(self):
        return self.base * self.height * 0.5

    def __str__(self):
        return f"Triangle({self.color},{self.base},{self.height}) 면적 =  {self.getArea()}"


# --- Main ----
Shape1 = Circle("yellow", 20)
Shape2 = Rectangle("red", 25, 11)
Shape3 = Triangle("blue", 25, 11)
Shape4 = Circle("red", 10)
Shape5 = Rectangle("yellow", 20, 25)

shape = [Circle("yellow", 20), Rectangle("red", 25, 11), Triangle("blue", 25, 11), Circle("red", 10),
         Rectangle("yellow", 20, 25)]

sumArea = 0
for i in shape:
    print(i)
    sumArea += i.getArea()

print(f"도형의 면적합계 = {sumArea}")
