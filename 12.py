"""

Write a program find all even number from the given input list and
display output as a list format. 

""" 


import random


list1 = [ ]

for num in range(50):

    list1.append(random.randrange(1,50))

print "List with Random Numbers: ", list1

Output_list = [ ]


for val in list1:

    if val%2 == 0:


        Output_list.append(val)

print "Even Numbers from Random List: ", Output_list




        
