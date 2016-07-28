from sys import argv # this is importing the argument variable identified below
from os.path import exists # this is looking into the current path and importing the command 'exits' to see if the specified file in the path exists

script, name, filename = argv # these are the varibles that make up my argument variable, which adds additional items into the sctipt 
print
print
print "Lets begin by opening the poem you have written and seeing if it good!" # simple printing of text  
print 
print "How do you feel about your poem? Do you think it is good?\nPlease let me know below." # this is printing, with a line break
poemgood = raw_input("> ") # raw input variable, this is taking how I feel about the poem
print
print "%r, I see you think your poem is %s." % (name, poemgood) # first operator is taking the name from argv variable, then response from poem good raw input vatiable
print
print "Ok %r, lets see this poem you wrote! I am going to read you poem titled %r below." % (name, filename) # name from argv line, filename from argv variable, entered in the command line
print "If you are ok with lettimg me read your poem, please press RETURN!" # printed string
raw_input("?") # blank raw input with no assigned variable, just need to press enter
print
poemopen = open(filename) # setting up the variable to open the file name, the item is filename
print "Your poem reads the following:" # string of text
print poemopen.read() # print poemopen open exectues the varabile that opens the filname, from argv, and the .read reads the target 
poemopen.close # this now closed the file, assignes the close function to the poemopen varabile which opend the file taken from the argv
print "Well %r, since you do not really like your poem, how about we work on another one?" % name # first operator taking name, simple string
raw_input("?") # simple raw input, just need to press enter 
print
print "Great! Please enter the name of your other file below." # now I am asking for the name of the file for the otehr poem that i want to open
newpoem = raw_input("> ") # this is the variable that is capturing the name of the new poem file that is opened
print
print "Ok, the name of your other poem is %r." % newpoem # this pulls the rawinput variable, is the name of the file i typed in 
print "Lets go ahead and read that wonderful poem of yours %r." % name # formatter pulling info from the argv variable 
print 
print "Your other poem reads the following:"
poem_open = open(newpoem) # opening in the a mode so we can append and add code on the end vs write over it
print poem_open.read() # opend the other poem and read it with the dot operator
print
print "Hmm, that is a pretty crude poem %r. Lets add some more line to it and see if we can make it nice" % name # pulling the name from the argv variable
poem_open.close() # closing out the poem after reading it, now ready to append it
poemwrite = open(newpoem, 'a') # opened the poem again to append
print "Please enter some new lines for your poem below!"
line1 = raw_input("Line 1: ") # getting multiple strings for varaibles here via the raw input function
print
line2 = raw_input("Line 2: ")
print
line3 = raw_input("Line3: ")
print
print "Ok, let me just read your lines real quick and see how I like them!"
print """
Your first line reads '%r'.\nYour second line reads '%r'.\nYour third line reads '%r'. 
""" % (line1, line2, line3)
print # reading back the lines i typed above in the raw input varables using formatters and the variable names
print "If you are ok with adding these as your new lines, please press RETURN."
raw_input("?") # just a blank raw input
print "Ok, I am adding the lines now!"
print "Adding! " * 10
poemwrite.write("\n"), poemwrite.write(line1), poemwrite.write("\n"), poemwrite.write(line2), poemwrite.write("\n"), poemwrite.write(line3)
poemwrite.close() # now it is writing each of the variables from raw inputs to the poemwrite variable which was opened with the poem write varaible, now it can be written to with the established a to specify I am appending it
print # closed out the poem after appending it, can be reopened again below to read
print "Ok %r, I have added your new lines to your great poem, to try to make it more nicer." % name # pulling name from the argv with the formatter
print
print "Now, lets go ahead and read that nice new poem of yours!"
print
print "Are you ready to read?"
raw_input("?")
print
readnewpoem = open(newpoem) # now i am opening up the new poem again, from the original rawinput of it, but new varaible to open it for read again
print readnewpoem.read() # reading with the dot operator
print
readnewpoem.close() # closing out the poem after reading it again
print
print "If you would like to continue into the next section, please hit RETRUN."
raw_input("RETRUN ")
print
print "Ok lets go ahead and copy your updated poem to a new file!\nThis will surley be a better location to store the file!" # line break in this one
print 
print "If I remmember correctly, the name of your new poem is %r." % newpoem # formatter puling varable, this is the original raw input variable
print "Ok, I have now opened up your new poem file again."
poemcopy = open(newpoem) #that poem is now open again
print 
print poemcopy.read() # now it is read again
print "Your poem %r is currently %d bytes long!" % (newpoem, len(newpoem)) # pulling newpoem name from varaibe obove, using len function on it to determine its lenghts in bytes 
print
print "Please enter the file you would like to copy to below:" # now i am making a rawnput variable to get the file name that i want to copy to 
copyto = raw_input("> ") # got that new filename destination here
print
print "Ok, you want to copy your poem %r to the file '%r'." % (newpoem, copyto) # new poem name as entered into the variable above, also the newest raw input variable
print
copyopen = open(copyto) # now opening the file i am copying to
print "Lets see if there is anything in this file." 
print
raw_input()
print "Does this file exist? %r" % exists(copyto) # pulling the exists action from the path above, checking against the current path to see if the file exists or can be run
print
print "Ok, and let me read what is in this file below:."
print
print copyopen.read() #i have not copied anything to this file yet, i am just reading it here
print
print
print "Now that the I confirmed the file's existence and read it,\nlets go ahead and copy your updated poem to it."
poemcopy.close() # closing the copy file after reading the contents of it and confirming that it exists
copyopen.close() # also closed the variable that originally opend the poem 
print "Please press RETURN to continue."
raw_input("RETURN ")
transfer1 = open(newpoem) # opened that new poem again 
transfer1read = transfer1.read() #now mad a variable that reads the opened file
transfer2 = open(copyto, 'w') # opening the desination file for writing too, gonna completely erase everything and write to the file 
transfer2.write(transfer1read) # writing the read file original to the destination file
transfer1.close()
transfer2.close # closing it all out 
print "Hello World - Brandyn Eckhart" 
