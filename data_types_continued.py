# String

s = "I am a string."
print(type(s))            # Will say str

# Boolean

yes = True                # Boolean True
print(type(yes))

no = False
print(type(no))           # Boolean false
print(" ")

# Lit  -- ordered and changeable

alpha_list = ["a", "b", "c"]    # List initialization
print(type(alpha_list))         # Will say tuple
print(type(alpha_list[0]))	     # Prints the type of the 0'th element of the list! (str)
alpha_list.append("d")          # Will add a "d" to fthe list end
print(alpha_list)               # Will print list
print(" ")

# Tuple -- ordered and unchangeable

alpha_tuple = ("a", "b", "c")   #Tuple initialization
print(type(alpha_tuple))        # Will say tuple
print(" ")

try:                                          # Attempt the following line:
	alpha_tuple[2] = "d"                         # Won't work and will raise TypeError
except TypeError:                             # When we get as TypeError
	print("We can't add elements to tuples!")    # Print this messqge
print(alpha_tuple)                            # Will print tuple
