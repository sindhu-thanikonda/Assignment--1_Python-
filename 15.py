"""

Take two input strings from the user and
concatenate two given strings by omitting the first character. 

""" 


str1 = raw_input("Enter First String: ")

str2 = raw_input("Enter Second String: ")


print str1[1:]
print str2[1:]

print "Final String with Omiting Characters: ", str1[1:] + str2[1:]







