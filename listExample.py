# Create a list of integers
a = [40, 12, 30, 50]

# Find the length of the list 'a' and print it
print(len(a))

# Append integer 7 to the end of the list 'a' and print the modified list
a.append(7)
print(a)

# Sort the list 'a' in ascending order and print the modified list
a.sort()
print(a)

# Remove the integer 50 from the list 'a' and print the modified list
a.remove(50)
print(a)

# Insert integer 50 at index location 2 in the list 'a' and print the modified list
a.insert(2,50)
print(a)

# Remove the last element from list 'a' and print the modified list
a.pop()
print(a)

# Find the index of integer 50 in the list 'a' and print it
print(a.index(50))

# Count the number of occurrences of integer 30 in the list 'a' and print it.
print(a.count(30))

# Reverse the order of elements in the list 'a' and print the modified list
a.reverse()
print(a)
