"""

Write a program join each and every character from the given
string with hyphen(-)
Example: 
Input_str = “PYTHON”
Output = P-Y-T-H-O-N

Note: Please Don’t use join () function.



""" 


Input_str = "PYTHON"

Output_str = " "
X = len(Input_str)
val = 0 

for ch in Input_str:

    if (X-1) != val:

        Output_str = Output_str + ch + "-"


    else:

        Output_str = Output_str + ch

    val += 1 # val = val +1  

    

print "String Separated with Hypen: ", Output_str






