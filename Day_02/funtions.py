def add_and_sumtract(a,b):
    mysum= a+b
    mydiff=a-b
    return(mysum,mydiff)

print(add_and_sumtract(23,15))     # (38, 8)
print(add_and_sumtract(43,13))     # (56, 30)

print(type(add_and_sumtract))      # <class 'function'>


def modify(mylist):
    mylist[0] *= 10
    return(mylist)
L = [1, 3, 5, 7, 9]
M = modify(L)
print(M is L)     #True


def intersect(s1,s2):
    res=[]
    for x in s1:
        if x in s2:
            res.append(x)
    return res

y= intersect([1,2,3,4,5],[3,4,5,6,7])
print(y)     # [3, 4, 5]

import random
print(random.choice("abcdefgh"))   # e
print(random.choice("abcdefgh"))   # a


def is_vowel(letter):
    """This is vowel function is checked whether input is vowel, Padme"""
    if letter in "aeiouy":
        return(True)
    else:
        return(False)

print(is_vowel('4'))

help(is_vowel)


