numbers=[1,3,3,5,3,4,6,4,6,4,6,6,4,9,8,9]
unic=[]

for num in numbers:
    if num not in unic:
        unic.append(num)

print(unic)

