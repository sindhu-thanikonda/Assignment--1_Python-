"""

Write a program create a random list of length 10 and
print all the elements except the elements which are divisible by 4.


""" 

list1 = [ ]    
val = 0

for str1 in range(10):

    str1 = raw_input("Enter Random List: ")
    print "Random String: ", str1

    val = len(str1)

    print "Length of String: ", val

    if val%4 != 0:


        list1.append(str1)

print "List with Non_Divisibles of 4: ", list1


"""


list1 = [ ]    
val = 0

for str1 in range(10):

    str1 = raw_input("Enter Random List: ")
    print str1

    list1.append(str1) 

    val = len(str1)

    print val

    if val%4 == 0:


        list1.pop()

print list1

"""










