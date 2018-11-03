"""

Write a program create 3x3 matrix using python.
Take all the elements from the user.
And also print the sum of diagonal elements from created matrix. 



""" 
x = int(raw_input("Enter number of rows in a matrix: "))
y = int(raw_input("Enter number of columns in a matrix: "))

list1 = [] 
num = 0 
 
#  Code for 3 * 3 Matrix 

print "Choosed {} * {} Matrix ".format(x, y)

for i in range(x):
    mat = []   
    for j in range(y):
        mat.append(int(raw_input("Enter the elements for Matrix: ")))    
    print "The {} Matrix is {} " .format(i+1, mat)    # Prints Individual Matrix 
    list1.append(mat)



print "The Matrix List: ", list1 # Prints the complete Matrix 


# Code for Sum of Diagonals in a Matrix


for k in range(x):

    for q in range(x):

        if k == q:
            num = num + int(list1[k][q])


print "Sum of all Diagonals: ", num   #   Prints Sum of Diagonals 




