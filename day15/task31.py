class RequireToString(type):

    def __new__(cls, name, bases, attrs):
        if '__str__' not in attrs:
            raise TypeError(f"Class '{name}' must define a __str__ method.")
        return super().__new__(cls, name, bases, attrs)

# Example of a class that correctly defines __str__
class MyStringClass(metaclass=RequireToString):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"MyStringClass with value: {self.value}"

# Creating an instance of the valid class
my_instance = MyStringClass("hello")
print(my_instance)

# Example of a class that does NOT define __str__
try:
    class MyBrokenClass(metaclass=RequireToString):
        def __init__(self, value):
            self.value = value
except TypeError as e:
    print(f"Error during class creation: {e}")