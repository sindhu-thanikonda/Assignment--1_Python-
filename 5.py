"""

WAP replace each string with an integer value in a given list of strings.
The replacement integer value should be sum of ascci values of each character of the same string. 
holy_rivers =["Ganges", "Godavari", "Brahmaputra", "Narmada", 
              "Yamuna", "Mahanadi", "Kaveri”, “Tapti"]
Hint: To get the ascii value of a charcter we need to use ord() function
Ex: ord("A") returns an integer value i.e 65- ascci value of A


""" 

holy_rivers =["Ganges", "Godavari", "Brahmaputra", "Narmada", 
              "Yamuna", "Mahanadi", "Kaveri", "Tapti"]


Input_list = holy_rivers 

length = len(holy_rivers)

print "Total Length of List: ", length

X = 0 

for i in holy_rivers:

    print "Iterating Value: ", i

    num = 0
    
    
    for j in i:

        print j

        val = ord(j)
        print val

        num = num + val

    print "sum of Strings: ", num

    print "=="*20

    print " Value of X: ", X 

    holy_rivers[X] = num
    
      

    X = X +1 
    
print "=="*20

print "The Input List with Strings: ", Input_list

print "=="*20 
 
print "The intergers values for the Given List: ", holy_rivers







        
