"""

Write a program change the given input list by  doing rotate left.
Ex: input = [4, 5, 6, 7]

output = [5, 6, 7, 4]


""" 


list1 = [4, 5, 6, 7]

X = len(list1)

print "Length of List: ", X

for val in range(len(list1)):

    i =  list1[0]
    
    j = list1[X-1]

    list1[0] = j

    list1[X-1] = i

    print "List While Swapping Left to Right: ", list1

    X = X - 1 


print "Final List After Swapping Left to right: ", list1




