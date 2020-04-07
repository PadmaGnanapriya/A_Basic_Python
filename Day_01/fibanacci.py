def fibacci(n):
    a=b=1
    for i in range(n):
        yield a
        a, b = b, a+b

print(sum(fibacci(1000)))