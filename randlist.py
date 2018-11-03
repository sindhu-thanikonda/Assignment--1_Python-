# WAP to create a Random List of 100 numbers and
# Also Print all Prime Numbers as Output



import random

rand_list = [ ]
for val in range(100):

    rand_list.append(random.randrange(1,100))

print "Original Random List: ", rand_list 





for num in rand_list:
    
    if num > 1:

        for val in range(2,num):

            if (num%val) == 0:

                break

        else:

            print "Prime Number: ", num



print "Prime Numbers From Random List: ", rand_list




        
