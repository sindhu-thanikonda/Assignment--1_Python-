"""

Write a program convert the following list to a dictionary.

X = [(“A”, 65), (“B”, 66), (“C”: 67), (“D”, 68)]

Note: Please don’t use dict() function. 


""" 


list1 = [("A", 65), ("B", 66), ("C", 67), ("D", 68)]
dict1 = { } 
list2 = [ ]

print "Length of List: ", len(list1)


for i in list1:

    print "Length of SubList: ", len(i)
    list2 = i


    dict1[list2[0]] = list2[1:]








print "Converted List to Dictionary: ", dict1 






