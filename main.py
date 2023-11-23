class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Function that demonstrates polymorphism
def print_area(shape):
    print(f"Area: {shape.area()}")

# Create instances of different shapes
circle = Circle(radius=5)
rectangle = Rectangle(length=4, width=6)
triangle = Triangle(base=3, height=8)

# Use the function with different types of shapes
print_area(circle)      # Output: Area: 78.5
print_area(rectangle)   # Output: Area: 24
print_area(triangle)    # Output: Area: 12.0
