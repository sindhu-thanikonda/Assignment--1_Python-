"""

WAP print all duplicated values in descending order from the given input list. 
Input_list = [401, 403, 409, 403, 453, 402, 438, 401, 444]

Output: 
Duplicated elements: [403, 401]


"""



Input_list = [401, 403, 409, 403, 453, 402, 438, 401, 444]

length = len(Input_list)

Duplicate_elements = [ ]

j = 0 

#print "Length of Input_list: ", length

print "List with Repeatative Values: ", Input_list
 
for val in Input_list:
    
    #print "Checking Input_list value: ", val

    j = j + 1   

    for i in Input_list[j:-1]:

        #print j
        
        #print "i value: ", i
        
        if val == i:

            Duplicate_elements.append(val)

print "Repeating Elements Before Reverse: ", Duplicate_elements


Duplicate_elements.reverse()
 

print "Repeating Elements after Reverse: ", Duplicate_elements















