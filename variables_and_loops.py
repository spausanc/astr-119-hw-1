import numpy as np		# We use numpy for lots of things

def main():
    i = 0				# Integers can be declared with a number
    n = 10				# Here is another integer
    x = 119.0			# Floating point nums are declared with a "."
    
    # We can use numpy to quickly make arrays
    y = np.zeros (n,dtype=float) #declares 10 zeros as floats using np

    # We can use 'for' loops to iterate through a variable
    for i in range(n):					#i in range [0, n-1]
        y[i] = 2.0 * float(i) + 1.0		#set y=2i+1 as floats

    # We can iterate through the y elements one by one
    for y_element in y:
        print (y_element)

# Execute the main function
if __name__ == "__main__":
    main()
	