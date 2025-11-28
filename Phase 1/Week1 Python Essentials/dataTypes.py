# Demonstration of list operations in Python
# mutable sequence type
numbers = [10, 20, 30, 40, 50]
print("Original list:", numbers)

print("Second element:", numbers[1])
print("Last element:", numbers[-1])
numbers[2] = 35
print("Modified list:", numbers)

numbers.append(63)
numbers.append(43)
print("List after appending:", numbers)
numbers.remove(20)
print("List after removing 20:", numbers)
numbers.sort()
print("Sorted list:", numbers)
numbers.reverse()
print("Reversed list:", numbers)
print("Length of the list:", len(numbers))
# few other list methods can be explored similarly
# these are few more methods: extend(), insert(), pop(), clear(), count(), index(), copy() which can be explored further like these.

# Demonstration of tuple operations in Python
# immutable sequence type
coordinates = (10.0, 20.0)
print("Original tuple:", coordinates)
print("First element:", coordinates[0])
print("Second element:", coordinates[1])
# tuples are immutable, so we cannot modify them directly
# but we can create a new tuple based on existing one
new_coordinates = (coordinates[0] + 5, coordinates[1] + 5)
print("New tuple:", new_coordinates)
print("Length of the tuple:", len(coordinates))
# few other tuple methods can be explored similarly
# these are few more methods: count(), index() which can be explored further like these.

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

# Demonstration of dictionary operations in Python
# key-value pairs
student = {"name": "Alice", "age": 21, "major": "Computer Science"}
print("Original dictionary:", student)
print("Name:", student["name"])
student["age"] = 22
print("Modified dictionary:", student)
student["graduation_year"] = 2023
print("Dictionary after adding graduation_year:", student)
del student["major"]
print("Dictionary after deleting major:", student)
print("Length of the dictionary:", len(student))
# few other dictionary methods can be explored similarly
# these are few more methods: keys(), values(), items(), get(), pop(), clear(), update() which can be explored further like these.

# Demonstration of string operations in Python
# immutable sequence of characters
greeting = "Hello, World!"
print("Original string:", greeting)
print("First character:", greeting[0])
print("Substring (0-5):", greeting[0:5])
upper_greeting = greeting.upper()
print("Uppercase string:", upper_greeting)
lower_greeting = greeting.lower()
print("Lowercase string:", lower_greeting)
print("Length of the string:", len(greeting))
# few other string methods can be explored similarly
# these are few more methods: strip(), split(), join(), replace(), find(), format() which can be explored further like these.

# Demonstration of frozenset operations in Python
# immutable version of set  
colors = frozenset(["red", "green", "blue"])
print("Original frozenset:", colors)
print("Length of the frozenset:", len(colors))
# frozensets do not support methods that modify the set
# but we can perform operations like union, intersection, difference
more_colors = frozenset(["yellow", "blue"])
union_colors = colors.union(more_colors)
print("Union of frozensets:", union_colors)
intersection_colors = colors.intersection(more_colors)
print("Intersection of frozensets:", intersection_colors)
difference_colors = colors.difference(more_colors)
print("Difference of frozensets:", difference_colors)
# few other frozenset methods can be explored similarly
# these are few more methods: isdisjoint(), issubset(), issuperset() which can be explored further like these.