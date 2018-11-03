"""
Write a program find all even numbers from the given list.

Input_List = [18.8, “Hyd”, 18, 26.9, 19, “BANG”, 26, 33.7, 25, “CHEN”]

Output = [18, 26]


""" 

Input_List = [18.8, "Hyd", 18, 26.9, 19, "BANG", 26, 33.7, 25, "CHEN"]

print "Length of List: ", len(Input_List)
  

list1 = [ ]


for ch in Input_List:

    if ch != str(ch) and ch%2 ==0:
        
        list1.append(ch)






print "Original List: ", Input_List

print "Final List With Even Numbers: ", list1 






