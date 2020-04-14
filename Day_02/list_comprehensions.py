y=sum([i**2 for i in range(3)])
print(y)    # 5    0+1+4

y=sum([i**2 for i in range(5)])
print(y)   # 30   0+1+4+9+16

y=sum([i**2 for i in range(6)])
print(y)   # 55   0+1+4+9+16+25

z=sum(i for i in range(1,10,2))
print(z)

z=sum([i for i in range(10) if i%2 == 1])
print(z)