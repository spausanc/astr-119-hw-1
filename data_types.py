import numpy as np     # Import numpy library

# Integers:

i = 10            # integer
print(type(i))    # Print out the data type of 1
print(" ")

a_i = np.zeros(i,dtype=int)	    #declare an array of ints. Otherwise will be floats
print(type(a_i))	            		#will return ndarray?
print(type(a_i[0]))		         	#will return integers of 64 bits?
print(" ")

# Floats:

x = 119.0 				   	#Floating point number
print(type(x))				#Print out the data type of x
print(" ")

y = 1.19e2		   			#floating 119 in sci. notation
print(type(y))				#print out the data type of y
print(" ")

z = np.zeros(i,dtype=float)	    #declare array of floats
print(type(z))			              	#will return nd array
print(type(z[0]))		            	#will return float64
