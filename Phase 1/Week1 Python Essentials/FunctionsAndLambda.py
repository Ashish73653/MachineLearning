# Defining the functions and lambda expressions
def greet(name):
    return f"Hello, {name}!"
print(greet("Alice"))
# Lambda function to add two numbers
add = lambda x, y: x + y
print(add(3, 5))

# parameters and default arguments
def power(base, exponent=2):
    return base ** exponent
print(power(4))        # Uses default exponent 2
print(power(2, 3))     # Uses exponent 3

# args and kwargs
def display_info(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)
display_info(1, 2, 3, name="Alice", age=25)


# Nested functions (a function defined inside another function).
def outer_function(msg):
    # inner_function is a nested function that "closes over" the variable `msg`.
    # This is a closure: inner_function can access `msg` from the outer scope.
    def inner_function():
        # Print the captured message. This uses the built-in print:
        # print(*values, sep=" ", end="\n", file=None, flush=False)
        print(msg)

    # Call the nested function so the message is printed when outer_function runs.
    inner_function()

# Call outer_function with a string -> inner_function prints it.
outer_function("Hello from the outer function!")

def make_adder(x):
    def add(y):
        return x + y
    return add

add5 = make_adder(5)
print(add5(10))  # Output: 15

add100 = make_adder(100)
print(add100(1))  # Output: 101



# Recursion example: Factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))  # Outputs 120

# Using map, filter, and reduce
from functools import reduce
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print("Squared numbers:", squared)
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)
product = reduce(lambda x, y: x * y, numbers)
print("Product of all numbers:", product)

# Docstrings and Annotations
def add_numbers(a: int, b: int) -> int:
    """Returns the sum of two numbers."""
    return a + b
print(add_numbers(3, 4))
print(add_numbers.__doc__)
print(add_numbers.__annotations__)

# Exploring built-in functions with functions
print("Using abs():", abs(-10))
print("Using round():", round(3.14159, 2))
print("Using sorted():", sorted([5, 2, 9, 1]))
print("Using sum():", sum([1, 2, 3, 4, 5]))

# Higher-order functions example
def apply_function(func, value):
    return func(value)
print(apply_function(lambda x: x ** 2, 6))  # Outputs 36
print(apply_function(str.upper, "hello"))  # Outputs "HELLO"

# Error handling in functions
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
print(safe_divide(10, 2))  # Outputs 5.0
print(safe_divide(10, 0))  # Outputs error message

# Exploring function attributes
def sample_function():
    """This is a sample function."""
    pass
print("Function name:", sample_function.__name__)
print("Function docstring:", sample_function.__doc__)
print("Function module:", sample_function.__module__)

# Lambda with multiple arguments
multiply = lambda x, y, z: x * y * z
print(multiply(2, 3, 4))  # Outputs 24

# Using lambda in sorting
points = [(1, 2), (3, 1), (5, 4), (2, 3)]
sorted_points = sorted(points, key=lambda point: point[1])
print("Points sorted by y-coordinate:", sorted_points)