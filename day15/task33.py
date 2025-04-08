class NegativeNumberException(Exception):
    """
    Custom exception raised when a negative number is encountered
    where a non-negative number is expected.
    """
    def __init__(self, number, message="Factorial is not defined for negative numbers"):
        self.number = number
        self.message = message
        super().__init__(self.message)

def nfactorial(n):
    """
    Calculates the factorial of a non-negative integer.
    Raises NegativeNumberException if n is negative.
    """
    if n < 0:
        raise NegativeNumberException(n)
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Example usage with exception handling
try:
    num1 = 5
    factorial1 = nfactorial(num1)
    print(f"Factorial of {num1} is: {factorial1}")

    num2 = -3
    factorial2 = nfactorial(num2)
    print(f"Factorial of {num2} is: {factorial2}")  # This line will not be reached

except NegativeNumberException as e:
    print(f"Error: {e.message}. The number was: {e.number}")

try:
    num3 = 0
    factorial3 = nfactorial(num3)
    print(f"Factorial of {num3} is: {factorial3}")

except NegativeNumberException as e:
    print(f"Error: {e.message}. The number was: {e.number}")