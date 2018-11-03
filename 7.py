"""

Write a program find the maximum number from the given input list
Input_list = [82, 62, 61, 54, 71, 89, 75, 73]

Note: Please dont use max() function to complete this. 


"""






list1 = [82, 62, 61, 54, 71, 89, 75, 73]


num = 0 

for val in list1:

    if num < val:

        num = val
        
        print "Checking for Max Number: ", num


print "The Maximum Number: ", num



