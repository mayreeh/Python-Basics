
str = "Learning-Python"

#indexing - returns the character in the specified position
print str[0] #returns L 
print str[-2] #returns the second ;last
"""
num = 67677
print num[0] #Error , indexing is only accessible in strings.
"""
num = "877"
print num[0] #returns 8 
####################################################################
#indices - returns a segment of an element
"""
L e a r n i n g - P y  t   h   o    n
0 1 2 3 4 5 6 7 8 9 10  11  12  13  14
"""
print str[0:1] #returns elements at position one(including) to elements at position 1 (Excuding) # returns L
print str[0 : 13] #returns Learning-Pyth
print str[::-1]  #reverses the string
