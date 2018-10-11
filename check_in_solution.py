# Include the Numpy Library
import numpy as np


# Define the main() function
def main():

	i = 0					# Declare an integer i
	x = 119.0				# Declare a float x
		
	for i in range(120):	# Loop i from 0 to 119, inclusive
		if((i%2) == 0):		# If i is even
			x += 3.				#add 3 to x
		else:				# If i is odd
			x -= 5.				#substract 5 from x

	s = "%3.2e" % x			# Make a string containing x with
							#sci. notation w/2 decimals places 
		
	print(s)				# Print s to the screen
	
# Now the rest of the program continues

if __name__ == "__main__":
	main()
	