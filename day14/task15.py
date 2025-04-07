import math

class Circle:
    def __init__(self, radius):
        if not Circle.is_valid_radius(radius):
            raise ValueError("Radius must be a positive number.")
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if not Circle.is_valid_radius(value):
            raise ValueError("Radius must be a positive number.")
        self._radius = value

    @property
    def circumference(self):
        return 2 * math.pi * self._radius

    @classmethod
    def from_diameter(cls, diameter):
        """Creates a Circle instance from a given diameter."""
        if not isinstance(diameter, (int, float)):
            raise TypeError("Diameter must be a number.")
        if diameter <= 0:
            raise ValueError("Diameter must be a positive number.")
        return cls(diameter / 2)

    @staticmethod
    def is_valid_radius(value):
        """Checks if a given value is a valid radius."""
        return isinstance(value, (int, float)) and value > 0

# Example usage:
if __name__ == "__main__":
    # Create a circle with a radius
    circle1 = Circle(5)
    print(f"Circle 1 radius: {circle1.radius}")
    print(f"Circle 1 circumference: {circle1.circumference:.2f}")

    # Check if a value is a valid radius
    print(f"Is 7 a valid radius? {Circle.is_valid_radius(7)}")
    print(f"Is -3 a valid radius? {Circle.is_valid_radius(-3)}")
    print(f"Is 'abc' a valid radius? {Circle.is_valid_radius('abc')}")

    # Trying to create an invalid circle
    try:
        invalid_circle = Circle(-2)
    except ValueError as e:
        print(f"Error creating circle: {e}")

    try:
        invalid_circle_from_diameter = Circle.from_diameter(0)
    except ValueError as e:
        print(f"Error creating circle from diameter: {e}")