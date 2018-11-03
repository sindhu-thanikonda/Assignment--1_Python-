# -*- coding: cp1252 -*-
"""

WAP combine all the first characters from given list representing a some of the compelling qualities of a great leader.   
qualities = [“Passion”, “Yearning”, “Transparency”, “Humble”,
“open-minded”, “Noble”] 


"""




Qualities = ["Passion", "Yearning", "Transparency", "Humble", "Open-minded", "Noble"]

str1 = []

for ch in Qualities:
    print ch
    print ch[0]
    str1.append(ch[0])

print "The New formed List with all First Characters: ", str1

    

