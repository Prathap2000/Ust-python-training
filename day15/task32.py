class RequireMethods(type):
    """
    A metaclass that enforces the definition of a list of methods
    in any class using it.
    """
    def __new__(cls, name, bases, attrs):
        required_methods = getattr(cls, '_required_methods', [])
        for method_name in required_methods:
            if method_name not in attrs:
                raise TypeError(f"Class '{name}' must define the method '{method_name}'.")
        return super().__new__(cls, name, bases, attrs)

    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        if not hasattr(cls, '_required_methods'):
            raise TypeError(f"Metaclass '{name}' must be initialized with a list of required methods.")

# Example: Using the metaclass directly (less common for specifying required methods)
# class BaseClass(metaclass=RequireMethods):
#     _required_methods = ['some_method']
#
#     def some_method(self):
#         pass

# More common way to use it: Creating a custom metaclass with the required methods
def require_methods(*method_names):
    """
    A factory function to create a metaclass that requires the specified methods.
    """
    class SpecificRequireMethods(RequireMethods):
        _required_methods = list(method_names)
    return SpecificRequireMethods

# Example using the factory function
RequireStringAndRepr = require_methods('__str__', '__repr__')
RequireStringReprAndDict = require_methods('__str__', '__repr__', 'to_dict')

class MyClass(metaclass=RequireStringReprAndDict):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f"MyClass({self.data})"

    def __repr__(self):
        return f"<MyClass object with data: {self.data}>"

    def to_dict(self):
        return {'data': self.data}

# This should work without errors
obj = MyClass({'a': 1})
print(obj)
print(repr(obj))
print(obj.to_dict())

class MyIncompleteClass(metaclass=RequireStringAndRepr):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Incomplete: {self.value}"

    # __repr__ is missing, so this will raise a TypeError
try:
    class AnotherIncompleteClass(metaclass=RequireStringAndRepr):
        def __init__(self, value):
            self.value = value

        # __str__ is missing, so this will raise a TypeError during class creation
        pass
except TypeError as e:
    print(f"Error during class creation: {e}")

try:
    class EvenMoreIncompleteClass(metaclass=require_methods('process', 'validate')):
        def __init__(self, data):
            self.data = data
        # Both 'process' and 'validate' are missing
except TypeError as e:
    print(f"Error during class creation: {e}")