# Define a dictionary data structure

# Dictionatries have key : value for the elements
example_dict = {
	"class"			:	"Astr 119",
	"prof"			:	"Brant",
	"awesomeness"	:	10
}
print(type(example_dict))	# Will say dict
print(" ")

# Get a value via key
course = example_dict["class"]
print(course)
print(" ")

# Change a value via key
example_dict["awesomeness"] += 1	# Increase awesomeness

# Print the dictionary
print(example_dict)
print(" ")

# Print dictionary element by element
for x in example_dict.keys():
	print(x,example_dict[x])
	