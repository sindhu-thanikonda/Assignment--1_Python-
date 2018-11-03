# -*- coding: cp1252 -*-
"""


Given dictionary representing a student name as a key and
corresponding value is a grade which he obtained in different subjects.
WAP update each dict value with average score
obtained by each student respectively. 
scores = {“Student1”: [65, 68, 59, 52, 69, 65, 55, 59], 
                 “Student2”: [60, 64, 60, 60, 88, 64, 68, 75],
                 “Student3”: [59, 72, 64, 62, 66, 68, 72, 73], 
                “Student4”: [82, 62, 61, 54, 71, 89, 75, 73]
                }

Output:
{“Student1”: 61.50 
   “Student2”: 67.37,
   “Student3”: 67.00,
    “Student4”:  70.87
   }

Note: Please don’t use sum() function to add the elements from a list



""" 


scores = { "Student1": [65, 68, 59, 52, 69, 65, 55, 59], 
                 "Student2": [60, 64, 60, 60, 88, 64, 68, 75],
                 "Student3": [59, 72, 64, 62, 66, 68, 72, 73], 
                "Student4": [82, 62, 61, 54, 71, 89, 75, 73]
                }





for key in scores:

    print scores[key]

    length = len(scores[key])

    num = 0 

    val = 0 
    
    for val in scores[key]:

        
        num = num + val

    print num/length 
      

    Average = num/length  

     

    scores[key] = Average  


print scores 




    








