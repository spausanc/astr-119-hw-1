# Python exceptions let you deal with
#unexpected results

try:
	print(a)	# This will throw and exception since a is not defined
except:
	print("a is not defined!")
	
# There are specific errors to help with cases
try:
	print(a)	# This will throw an exception since a is not defined
except NameError:
	print("a is still not defined!")
except:
	print("Something else went wrong.")
	
# This will break our program
#since a is not defined:
print(a)
