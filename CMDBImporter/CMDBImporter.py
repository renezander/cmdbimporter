#!/usr/bin/python
from petl import *
table1 = fromcsv('H:\example1.csv')
table2 = convert(table1, 'foo', 'upper')
table3 = convert(table2, 'bar', int)
table4 = convert(table3, 'baz', float)
print(look(table4))
