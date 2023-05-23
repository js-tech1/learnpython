# Create a dictionary with keys and values of different types
a = {"one": 1, 2.5: "flot", 8: "int"}

# Print the dictionary 'a'
print(a)

# Find the length of dictionary 'a' and print it
print(len(a))

# Get a list of all the keys in the dictionary 'a' and print it
print(a.keys())

# Get a list of all the values in the dictionary 'a' and print it
print(a.values())

# Get a list of all the (key, value) pairs in the dictionary 'a' and print it
print(a.items())

# Retrieve the value corresponding to key 2.5 from the dictionary 'a' and save it to variable 'data', then print it
data = a.get(2.5)
print(data)

# Remove the key-value pair corresponding to key 8 from the dictionary 'a' and print the modified dictionary
a.pop(8)
print(a)

# Remove a random key-value pair from the dictionary 'a' and print the modified dictionary
a.popitem()
print(a)

# Create another dictionary containing new key-value pairs, update dictionary 'a' with these new pairs and print the modified dictionary
b = {"one": 54, 88: 7.5}
a.update(b)
print(a)

# Create a new dictionary where all keys are "one" and their corresponding values are 12, print this new dictionary
print(a.fromkeys("one",12))

# Empty the dictionary 'a'
a.clear()

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
