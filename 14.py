"""

WAP replace each string from the given list with the same string
which is repeated with length of the string. 

Example: 
Input = [“A”, “AB”, “ABC”, “ABCD”]

Output = [“A”, “ABAB”,          “ABCABCABC”,“ABCDABCDABCDABCD”] 


""" 


Input = ["A", "AB", "ABC", "ABCD"]

num = 0

Output = [ ] 

for ch in Input:

    X = ""  
    val = len(ch)

    for i in range(val):

        X = X + ch 

    Output.append(X) 

        
    num = num + 1 

print "Original List: ", Input

print "List with Repeated Length of a String: ", Output




