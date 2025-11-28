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