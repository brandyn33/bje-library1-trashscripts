from sys import argv #from my system I am importing a argment variable that will be passd from th command line

script, name = argv #script is the name of my py file, name is the other item I enter in the prompt, here it is my name

def money(euro): #named my first function 								
	return euro * .91 #no printing for this function, just the return, which takes a value and assings it to a variable

def money2(ruble):
	return ruble * 65.80 #return makes a value available, does not print it to the console
#my variable here is ruble, which will be assinged with a varialbe below, the raw_input
def money3(yuan): # when the function is called in a variable assignment, 
	return yuan * 6.67

print "______________________________________________________________________________________________"
print
print "Good morning %r! Are you ready to check the trading prices for currency today?" % name
raw_input("Please Press Enter to Continue> ") #took the name from argv variable, which was populated in the command line
print
print "Excellent. Booting Dollar to Euro Conversion" #printing to the console, saw rawinputs to break things up and make this appear to be not total printing shit 
raw_input()
print
print
print "Please Enter Dollar Amount Below:"
print
conversion = money(int(raw_input("$> "))) # this is a varaibe assignement, I am assigning the variable to the function
print "The amount you entered is equal to %d Euros today." % conversion
print
print "Please Press Enter to Continue Conversions:"
raw_input(">ENTER ")
print
print "Excellent. Now Booting Conversion to Rubles."
print
print "Please Enter Dollar Amount Below:"
conversion2 = money2(int(raw_input("$> "))) # = assignes value to the variable (assingment operator), 2 things now happen. 1 - Runs whatever code is in the function, 2 - takes the return value from function and assings it to the variable
print "The amount you entered is equal to %d Rubles today." % conversion2
print
print "Please Press Enter to Continue Conversions:"
raw_input(">ENTER ")
print
print "Excellent. Now Booting Conversion to Yuan."
print
print "Please Enter Dollar Amount Below:"
conversion3 = money3(int(raw_input("$> ")))
print "The amount you entered is equal to %d Yuan today." % conversion3
print
print "Please see all values you entered today below:"
print
print "|Euros: %d| |Rubles: %d| |Yuan: %d| " % (conversion, conversion2, conversion3)
print
print "Please see a breif equation below following the order of operations.\nI will be dividing Yuan from Rubles, then adding Euros."
print
puzzle = conversion + (conversion2 / conversion3)
print puzzle
print "______________________________________________________________________________________________"
