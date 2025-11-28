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