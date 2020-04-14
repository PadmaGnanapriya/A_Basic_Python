# You can memorize this scope rule by the acronym LEGB.
# It may not be the catchiest acronym, but it works.
# Here's what the different letters stand for.
# L stands for "local," E stands for "enclosing function," G for "global,"
# and B stands for "built-in."


def increment(n):
    n += 1
    print(n)

n = 1
increment(n)
print(n)





def increment(n):
    n += 1
    return n

n = 1
while n < 10:
    n = increment(n)
print(n)