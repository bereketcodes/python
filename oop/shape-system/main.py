
# Build a Shape system:

# An abstract class Shape with an abstract method area()
from abc import ABC, abstractmethod



class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
    def __str__(self):
        return f"Triangle area = { self.area():.2f}"
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def __str__(self):
        return f"Rectangle area = { self.area():.2f}"          

shapes = [Triangle(10, 5), Rectangle(10, 5)]  # This will cause an error since Shape is abstract

for s in shapes:
    print(s)
    
def total_area(shapes):
    total = 0
    for s in shapes:
        total += s.area()
    return total

print(f"Total area = { total_area(shapes):.2f}")