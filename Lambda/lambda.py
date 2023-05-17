def square(n):
    return n ** 2
squares = map(square, range(1, 10, 2))  #first two values are min and max and third is position
squares
# returns map object
list(squares)