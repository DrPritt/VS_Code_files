import math

class Circle():
    def __init__(self, radius) -> None:
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2
    
    def perimeter(self):
        return math.pi * self.radius * 2
    
    def __str__(self) -> str:
        return f"Selle ringi raadius on {self.radius}"
    
class Square(Circle):
    def __init__(self, radius) -> None:
        super().__init__(radius)
        self.side = radius * 2

    def area(self):
        return self.side**2
    
    def perimeter(self):
        return self.side * 4
    
    def __str__(self) -> str:
        return f"Selle ruudu külje pikkus on {self.side}"

asked_radius = 5
circle1 = Circle(asked_radius)
square1 = Square(9)

asked_radius = 1 + circle1.radius

print(circle1)
print(asked_radius, circle1.area(), circle1.perimeter())


print(square1, "Pindala on",square1.area(), "ja ümbermõõt on",square1.perimeter())