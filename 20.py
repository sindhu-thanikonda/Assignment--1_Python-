"""

Write a program reverse each string from the given list and
finally reverse a list.

""" 

val = 0 


list1 = [raw_input("Enter a List: ")] 

list2 = [ ]


 
for ch in list1:

    text = " "
    len1 = len(ch)

    for i in range(len1):

        text = text + ch[len1-1]
        len1 = len1 - 1

    print "Reversed String: ", text

    list2.append(text)
        


print "Original List: ", list1
print "Reversed List: ", list2







