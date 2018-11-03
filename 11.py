"""

Write a program take 10 input strings of different lengths from the user and
store all the strings into a list and
display only odd length strings are the output in a list format.

"""


list1 = [ ] 
val = 0
list2 = [ ]

for str1 in range(10):

    str1 = raw_input("Enter a String: ")
    list1.append(str1) 
    print str1
    val = len(str1)
    print val
    if val%2 !=0:
        list2.append(str1)


print "Original List With 10 Strings: ", list1 # Original List with 10 Strings

print "Final List With Odd Length: ", list2  # List with Odd Length Strings 






