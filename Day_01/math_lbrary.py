import math
print(math.cos(math.pi))  # -1.0


nums = set([1, 1, 2, 2, 3, 3, 3, 4])
print(len(nums))   # 4


a=[1,2,3]
a[1]=4
print(a)   #[1, 4, 3]


# b=(1,2,3)
# b[1]=4
# print(b)   #This code contains an error. Set cant be update. No duplicate values


c = [1,2,3]
d = c
print(c == d)   #True
print(c is d)   #True


b = a[:]
print(a == b)  #True
print(a is b)  #False


y = [x**2 for x in range(5)]
print(y)  #[0, 1, 4, 9, 16]


x = 1
def my_function():
    x = 2
    print(x)   #1
print(x)       #2
my_function()
print(x)       #1


x = 1
while x < 5:
    x *= 2
print(x)   #8


for integer in (-1,3,5):
    if integer < 0:
    	print("negative")
    else:
    	print("non-negative")
# negative
# non-negative
# non-negative


x = 'String'
y = 10
z = 5.0
print(x + x) # StringString
print(y + y) # 20
print(y + x) # 
print(y + z) #