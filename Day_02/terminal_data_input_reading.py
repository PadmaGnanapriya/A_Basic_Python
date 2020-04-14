f_name=str(input('Enter your first name  : '))
s_name=str(input('Enter your second name : '))
age=int(input("Enter your age here    : "))
f_name=f_name.upper()
name_format="Mr/Mrs {name1:.1s}.{name2}, you are {age3} years old."
print(name_format.format(name1=f_name,name2=s_name,age3=age))