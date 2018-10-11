x = [0.0, 3.0, 5.0, 2.5, 3.7]    # Define an array
print(type(x))

# Remove the third element
x.pop(2)
print(x)

# Remove the element at the end 
x.remove(2.5)
print(x)

# Add and element at he end
x.append(1.2)
print(x)

# Get a copy
y = x.copy()
print(y)

# How many elements are 0.0
print(y.count(0.0))

# Print the index with value 3.7
print(y.index(3.7))

# Sort the list
y.sort()
print(y)

# Reverse sort
y.reverse()
print(y)

# Remote all elements
y.clear()
print(y)
