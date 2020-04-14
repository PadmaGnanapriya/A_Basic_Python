import sys

line = input()
split=line.split()
left=int(split[0])
opr=split[1]
right=int(split[2])
var=0

if opr=='+':
    val=left+right
elif opr=='-':
    val=left-right
elif opr=='*':
    val=left*right
elif opr=='/':
    if right==0:
        print("Zero Division Error")
        sys.exit()
    val=left/right
elif opr=='x':
    val=left*right
else:
    print("Unknown operator")
    sys.exit()
print("{line_expr} = {value:.2f}".format(line_expr=line, value=val))