# Create a tuple containing 5 integers
a = (34, 56, 87, 54, 23)
# Find the length of the tuple and print it
print(len(a))

# Count the number of times the integer 34 appears in tuple 'a' and print it
print(a.count(34))

# Find the index of integer 56 inside the tuple 'a' and print it
  print(a.index(56))

# Find the maximum value in tuple 'a' and print it
print(max(a))

# Find the minimum value in tuple 'a' and print it
print(min(a))

# Sort the tuple 'a', assign the sorted values back to 'a' as a new tuple, and print it
a = tuple(sorted(a))
print(a)

# Reverse the order of the tuple 'a' and print it without modifying the original tuple
print(tuple(reversed(a)))

# Create another tuple containing 3 integers
b = (6, 44, 566)

# Concatenate tuples 'a' and 'b', assign the new concatenated tuple to 'a', and print it
a += b
print(a)
