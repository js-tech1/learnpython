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
