#This progran HAS A LOT OF COMMENTS due to the fact that it is
#to be read by novices in Python.  

#This program reads in file WithTabs.txt as input 
#(it should be in the same directory as the program)  
#and copies its contents to output file
#NoTabs.txt (This output file will also be created in
#the same directory as the program).  In NoTabs.txt,
#each tab is replaced with an equivalent number of spaces 
#so that it looks the same. This is
#quite handy when submitting text to Canvas from a mac, since Canvas
#does not recognize the tabs from some mac programs.   
#This program also does not copy over superfluous blank chars at the 
#end of the lines of file WithTabs.txt.  (I worry that strange 
#issues can come up in Canvas when text is submitted 
#with superfluous blanks at the end of lines.)
#
#  Now I typed in the following two lines
#
#123456789
#    here
#
#and I used a tab to indent out to "here" on
#the second line.  
#So I would say a tab is 4 spaces, so I will replace each
#tab of the input file with four spaces.  

#-------------------------------

#We establish links to the only two files we work with.
#WithTabs.txt (that might have tabs) and NoTabs.txt, which
#should not exist when program is run.  NoTabs.txt should
#look like WithTabs.txt but all tab chars have been replaced with
#an equivalent number of spaces. 
#Currently we assume a tab is the same as SPACES_FOR_A_TAB  spaces. 
 
InputProgramFile = open("WithTabs.txt")
OutputProgramFile = open("NoTabs.txt","w")


SPACES_FOR_A_TAB = 4
# the number of spaces we wish to replace a tab with

#note: if we miss, it is still o.k., the spacing over is just
#a little different in the two files


listOfLines=InputProgramFile.readlines()
#listofLines now is a list where each element of the list
#is a line of WithTabs.txt

NumOfTabs = 0

# Looking below, variable LineIndex is first set to 0, then 1, then 2, etc.,
# up to the (number of lines in listofLines) - 1  .
# This matches how Python names the elements of a list.
# The elements range from 0 to the number of elements in the list
# minus 1,  (Because the fist element is called 0, not 1, the last element
# of a Python list is the ((number in list) - 1) element. 
# This is how "for" and "range" work in Python.  

for LineIndex in range(len(listOfLines)):
  TheLineOfProg = listOfLines[LineIndex]
  LineWithoutTabs = ""

# LineIndex will be 0 the first time in the loop, then 1, 2, etc.
# listOfLines[0] is  the first line of WithTabs.txt
# listOfLines[1] is  the second line of WithTabs.txt

# TheLineOfProg is set to a line of listOfLines . (The
# line we are working on right now).  
# We buid up LineWithoutTabs to be the same as TheLineOfProg 
# except that each tab is replaced with SPACES_FOR_A_TAB blanks.
  
# We loop through each char of TheLineOfProg and if the char is a tab,
# we loop for as many spaces represent a tab, and add that space
# to the end of LineWithoutTabs.  If the char is not a tab then we just
# add that char to the end of the LineWithoutTabs.
# Thus we build up LineWithoutTabs to be the line we want.  

  for i in range(len(TheLineOfProg)):   # for every line in WithTabs.txt
    if (TheLineOfProg[i] == "\t"):  #\t means tab in Python
      NumOfTabs = NumOfTabs + 1
      print("found one, we now have found ",NumOfTabs," tabs.")
      for j in range(SPACES_FOR_A_TAB):
        LineWithoutTabs=LineWithoutTabs+" "
    else:
        LineWithoutTabs=LineWithoutTabs+TheLineOfProg[i]

  # rstrip gets rid of white space at the end of a line.
  # We do that so that we don't have something funny there
  # that might throw things off when submitting to Canvas

  LineWithoutTabs = LineWithoutTabs.rstrip()


  print(LineWithoutTabs, file=OutputProgramFile)
  #this ends our loop

OutputProgramFile.close()
print("done")
