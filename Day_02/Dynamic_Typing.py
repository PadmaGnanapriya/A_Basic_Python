L = [1,2,3,4]
M = [1,2,3,4]
print(L ==M)   #True
print(L is M)  #False
print(id(L))   #46810616
print(id(M))   #46811776

L1 = [2,3,4]
L2 = L1
L2[0] = 24
print(L1)    # [24, 3, 4]

# There are two types of copies that are available.
# A shallow copy constructs a new compound object
# and then insert its references into it to the original object.
# In contrast, a deep copy constructs a new compound object and then
# recursively inserts copies into it of the original objects.