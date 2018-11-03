"""

Given a string of even length and
print the output as string contains
last half added with first half of the given string


""" 



Input_str = "AngryBirds"


length = len(Input_str)

print "Length of Input String: ", length

val = 0

First_half, Last_half, Output_str = "", "", ""  


for ch in Input_str:

     
    
    if ((length/2)-1) > val:

        First_half = First_half + ch


    else:

        Last_half = Last_half + ch

    val = val + 1  


Output_str = Last_half + First_half

print "Original String: ", Input_str


print "String after lasthalf with firsthalf: ", Output_str


        
