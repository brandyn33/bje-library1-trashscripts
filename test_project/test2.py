def fruits(arg1, arg2, arg3, arg4): # naming my function and listing the argument variable that will be inside it, I am also naming the variables that will be in my function
	print "Pleae see the list of fruits below:"
	print "Fruit1: %r, Fruit2: %r, Fruit3: %r, Fruit4: %r." % (arg1, arg2, arg3, arg4)
#the above is the unpacking of the function
#Now I am going to call out the functions that are listed above
fruits("Bannana", "Orange", "Apple", "Pear") #calling out the funtion above

def vegetables(veg1, veg2, veg3): # I have my three varable here, and I just want them printed in a simple string below
	print "%r, %r, %r." % (veg1, veg2, veg3) #setting up the unpacking strcture here, just string and adding the varables in

vegetables("Carrots", "Lettuce", "Celery") #now calling on the function, can add any text in the strings here
print
print "Hello World!"
print
def cars(car1, car2): #doing the same thing as above 
	print "My favorite car is a %r, and my other favorite car is a %r!" % (car1, car2)

cars("BMW", "Audi")
print
print
def math(var1, var2): #I am defining two varables for my function here, and will make them raw inputs 
	print "If I add my variables they equal", var1 + var2 # unpacking the function here, will be a string then adding the two varables of the function together, going to conver them to integers belwo
print "Please enter two numbers below"
math(int(raw_input("> ")), int(raw_input("> "))) #calling out the funcion, rawinputs for both of the variables in the function, string converted to integer
print
def ilike(like1, like2, like3):
	print "I like to drive my", like1, "In the", like2, "Listening to", like3 #unpacking strcture of the funcation
print
print "Please enter respones below to complete a sentance."
ilike(raw_input("Favorite Car> "), raw_input("Favorite Season> "), raw_input("Favorite Song> "))
print #calling on the function, placing rawinputs for each of the functions varaibles
print "___________________________________________________________________________________________________"
print "Hello World" 
print
def mycars(car1, car2, mph1, mph2):
	print "My %s is fast." % car1
	print "My %s is also really fast" % car2
	print "It goes %d MPH" % mph1
	print "My other one goes %d MPH too!" % mph2

mycars("BMW", "Mini", 200, 200)
print
print "Please enter the information below."
mycars(raw_input("Name a car> "), raw_input("Name another car "), int(raw_input(">MPH ")), int(raw_input(">MPH ")))
print
print
cars1 = "Audi"
cars2 = "BMW"
fast = 500
faster = 1000
print
mycars(cars1, cars2, fast, faster)
print
mycars (cars1 + cars2, cars2, 100, int(raw_input("> ")))
