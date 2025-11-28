# Conditionals
if True:
    print("This is true")

if False:
    print("This is false")
else:
    print("This is else block")

x = 10
if x > 0:
    print("Positive number")
elif x == 0:
    print("Zero")
else:
    print("Negative number")

# Loops
# While loop
count = 0
while count < 5:
    print("Count:", count)
    count += 1
# For loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)
# Looping through a range
for i in range(3):
    print("Number:", i)
# Nested loops
for i in range(2):
    for j in range(2):
        print("i:", i, "j:", j)
# Loop control statements
# Break statement
for i in range(5):
    if i == 3:
        break
    print("Break example, i:", i)
# Continue statement
for i in range(5):
    if i == 2:
        continue
    print("Continue example, i:", i)
# Pass statement
for i in range(5):
    if i == 4:
        pass  # Placeholder for future code
    print("Pass example, i:", i)
# Using else with loops
for i in range(3):
    print("Loop with else, i:", i)
else:
    print("Loop completed without break")
# Demonstration of set operations in Python
# unordered collection of unique elements
fruits = {"apple", "banana", "cherry"}
print("Original set:", fruits)
fruits.add("orange")
print("Set after adding orange:", fruits)
fruits.remove("banana")
print("Set after removing banana:", fruits)
fruits.add("apple")  # adding duplicate element
print("Set after adding duplicate apple:", fruits)
print("Length of the set:", len(fruits))
# few other set methods can be explored similarly 
# these are few more methods: update(), discard(), pop(), clear(), union(), intersection(), difference() which can be explored further like these.

# Comprehensions
# List comprehension
squares = [x**2 for x in range(5)]
print("List comprehension (squares):", squares)
# Set comprehension
unique_squares = {x**2 for x in range(5)}
print("Set comprehension (unique squares):", unique_squares)
# Dictionary comprehension
square_dict = {x: x**2 for x in range(5)}
print("Dictionary comprehension (squares):", square_dict)
# Generator comprehension
square_gen = (x**2 for x in range(5))
print("Generator comprehension (squares):", list(square_gen))
# few other dictionary methods can be explored similarly
# these are few more methods: keys(), values(), items(), get(), popitem(), clear(), update() which can be explored further like these.