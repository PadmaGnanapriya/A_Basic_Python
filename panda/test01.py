import pandas
import numpy

print("\n\n Table.0")
listx = [10, 20, 30, 40]
table0 = pandas.DataFrame(listx)
print(table0)

print("\n\n Table.1")
data = [{'a': 11, 'b': 12}, {'a': 13, 'b': 14, 'c': 15}, {'b': 17, 'c': 18, 'd': 19}]
table1 = pandas.DataFrame(data)
print(table1)

print("\n\n Table.2")
series1 = pandas.Series([80, 90, 78], index=['maths', 'chemistry', 'physics'])
series2 = pandas.Series([92, 42, 98], index=['maths', 'chemistry', 'physics'])
series3 = pandas.Series([80, 88, 68], index=['maths', 'ict', 'physics'])
series4 = pandas.Series([72, 97, 72], index=['maths', 'chemistry', 'physics'])

table = pandas.DataFrame({
    'Pasindu': series1,
    'Padma': series2,
    'Anjana': series3,
    'Sunanda': series4
})
print(table)



print('\n After delete Pasindu')
table.pop('Pasindu')
print(table)

        #    After delete Pasindu
        #              Padma  Anjana  Sunanda
        #   chemistry   42.0     NaN     97.0
        #   ict          NaN    88.0      NaN
        #   maths       92.0    80.0     72.0
        #   physics     98.0    68.0     72.0