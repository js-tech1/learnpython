scores = {
    "Jane" : 30,
    "Joe" : 20,
    "George": 30,
    "Hellena": 90,
}
# part one loop for printing as it is
for name in scores.keys():
    print(f"{name:8} {scores[name]}")


print('')

# part two for ascending order
for name in sorted(scores.keys()):
    print(f"{name:8} {scores[name]}")


print('')

# part three for values only
for val in sorted(scores.values()):
    print(f"{val:8}")

print('')

# part three for descending order
for name in sorted(scores.keys(), key=lambda x: scores[x]):
    print(f"{name:8} {scores[name]}")