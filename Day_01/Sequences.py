from django.template import library

print( (1,2,3)[-0] )              # 1
print( (1,2,3)[-0:0] )            # ()
print( (1,2,3,4,5,6,7,8)[-1] )    # 8
print( (1,2,3,4,5,6,7,8)[-0:3] )  # (1, 2, 3)
print( (1,2,3,4,5,6,7,8)[2:5] )   # (3, 4, 5)


#____List____#
numbers=[2,4,6,8,10,18]
print(numbers[3])     #8
print(numbers)        #[2, 4, 6, 8, 10, 18]
numbers.append(20)
print(numbers)        #[2, 4, 6, 8, 10, 18, 20]
x=[20,26,26]
numbers=numbers+x
print(numbers)        #[2, 4, 6, 8, 10, 18, 20, 20, 26, 26]
print(type(numbers))  #<class 'list'>
numbers.reverse()
print(numbers)      #[26, 26, 20, 20, 18, 10, 8, 6, 4, 2]


list01=['Padma','Pasindu','Sunanada','Gitmi','Ovindu','Ravindu']
list01.sort()
print(list01)         #['Gitmi', 'Ovindu', 'Padma', 'Pasindu', 'Ravindu', 'Sunanada']
list02=['Siluna','Padma','Dewinda','Ashen','Amal','Yohan']
sorted_list02=sorted(list02)
print(list02)         #['Siluna', 'Padma', 'Dewinda', 'Ashen', 'Amal', 'Yohan']
print(sorted_list02)  #['Amal', 'Ashen', 'Dewinda', 'Padma', 'Siluna', 'Yohan']


#____Tuples_____
T=(1,2,3,3)
print(T.count(3))   # 2
print(sum(T))       # 9
print(len(T))       # 4
c=(1,2,3)
print(type(c))   # <class 'tuple'>
c=(8)
print(type(c))   # <class 'int'>
c=(8,)
print(type(c))   # <class 'tuple'>


#___Ranges_____
#Ranges take up less memory than lists because they do not hold all the numbers simultaneously.
print(range(5))             # range(0, 5)
print(list(range(5)))       # [0, 1, 2, 3, 4]
print(list(range(5,17)))    #[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
print(list(range(5,17,2)))  #[5, 7, 9, 11, 13, 15]



#____sets____Frozen_sets__________
ids=set()
ids=set([1,2,3,4,5,5,5,6,7,7,8])
print(ids)   #{1, 2, 3, 4, 5, 6, 7, 8}
print(len(ids))  #8
ids.add(9)
ids.add(10)
print(ids)   #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
ids.pop()
ids.pop()
print(ids)  #{3, 4, 5, 6, 7, 8, 9, 10}
human=set(range(10))
print(human)          #{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
male=set([2,4,6,8,10])
female=human-male
print(female)         #{0, 1, 3, 5, 7, 9}
female.add(6)
print(male|female)    #{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(male & female)  #{6}
#count unic letters
print(len(set('aaaaffffsssaaAAAssss')))   # 4
    # Let sets x={1,2,3} and y={2,3,4}. How could you get {4} from x and y using basic set operations?
    # y-x
    # Consider again sets x={1,2,3} and y={2,3,4}. How could you get {2, 3} from x and y using basic set operations?
    # x&y
    # Consider again sets x={1,2,3} and y={2,3,4}. How could you get {1, 4} from x and y using the provided set methods?
    # (x|y)-(x&y)
    # Consider again sets x={1,2,3} and y={2,3,4}. Which of the following lines of code will determine if all elements of x are in y?
    # x.issubset(y)


#____________Dictionaries_________
age={}
age=dict()
age={"Padma":23,"Pasindu":22,"Sunanada":24}
print(age["Sunanada"])   # 24
age["Sunanada"]+=2
print(age["Sunanada"])   # 26
print(age.keys())        # dict_keys(['Padma', 'Pasindu', 'Sunanada'])
print(age.values())      # dict_values([23, 22, 26])
print(type(age))         # <class 'dict'>
print(type(age.keys()))         # <class 'dict_keys'>
print(type(age.values()))         # <class 'dict_values'>

#___Strings____
k='Python'
print(len(k))                               # 6
kk=k+k
print(kk)                                  # PythonPython
print(k*4)                                 # PythonPythonPythonPython
# k1=k+3.7
# print(k1)
k2=k+str(3.7)
print(k2)                                  # Python3.7
print(k.replace('on','aaa'))               # Pythaaa
print(k.upper())
print(('aE23weWD qStfFGfDe').lower())      # ae23wewd qstffgfde
print(('aE23weWD qStfFGfDe').title())      # Ae23Wewd Qstffgfde
print("".join([str(i) for i in range(10)]))  #0123456789
print(('aE23weWD qStfFGfDe').split(' '))    # ['aE23weWD', 'qStfFGfDe']
print(dir('str'))  #['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__',
                   # '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', 'translate',
                   #'__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', 'upper'
                   # '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__',  , 'zfill'
                   # '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__',
                   # '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold',
                   # 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map',
                   # 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower',
                   # 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower',
                   # 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition',
                   # 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', ]
