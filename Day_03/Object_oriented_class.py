class MyList(list):
    def remove_min(self):
        self.remove(min(self))
    def remove_max(self):
        self.remove(max(self))

x=[10,3,5,2,4,2,9,3,4,10,1,1]
y=MyList(x)
print(y)
y.remove_max()
print(y)
y.remove_min()
print(y)
#This functions will delete first max and min value only.
# If there are duplicates it not care that.



class NewList(list):
    def remove_max(self):
        self.remove(max(self))
    def append_sum(self):
        self.append(sum(self))

x = NewList([1,2,3])
while max(x) < 10:
    x.remove_max()
    x.append_sum()

print(x)