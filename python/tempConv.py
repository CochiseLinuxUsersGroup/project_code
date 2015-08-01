#paulbe practice code
#Temp converter

print "Convert from celcius to farenheidt or vise-versa"

#Prints statement and uses user input to define a variable 'var'
var = raw_input("Input C to convert from celcius to farenheidt or F to convert from farenheidt to celcius: ")


#Checks if 'var' is equal to f or F
#If true then it ask user to input temp in Farenheidt setting it equal to the temp variable.
#Then converts f into c and prints the results.
if var == 'f' or var == 'F':
	temp = raw_input("Temp in F?")
	convf = (int(temp) -32) * 5.0 / 9
	print "In celcius that is: ", convf


#Checks if 'var' is equal to c or C
#If true then it asks user to input temp in Celcius setting it equal to the temp variable.
#Converts c into f and prints results.
	
elif var == 'c' or var == 'C':
	temp = raw_input("Temp in C?")
	convc = (int(temp) * 9) / 5.0 + 32
	print "In farenheidt that is: ", convc


#Checks for dummies that cant read
else:
	print "Please enter C or F to use"
