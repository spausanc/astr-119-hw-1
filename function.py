import numpy as np
import sys	            #Gives access to the command line arguments

# Define a function that returns a value
def expo(x):
	return np.exp(x)	    # Return the np e^x function
	
# Define a subroutine that does not return a value
def show_expo(n):
	for i in range(n):
		print(expo(float(i)))    # Call the expo function
	
# Define a function 
def main():
	n = 10    # Provide a default function for n

	# Check if there is a comnand line argument provided
	if(len(sys.argv)>1):		#len tells you the length of the array :o
		n = int(sys.argv[1])	#sys.argv is the variable arguments in the system?
							               	#this lets us grap the argument inputted in the command line,
							               	#and put it in the array as an integer
	show_expo(n)          # Call the show_expo subroutine
	
	
# Run the main function
if __name__ == "__main__":
	main()
	