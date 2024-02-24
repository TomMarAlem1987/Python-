'''Class Exercises:
Transforming Data: MAP

Convert this list of temperatures from Celsius to Fahrenheit: 32, -17, 40, 5, -7, 20, -1, 16, -16, 4 Celsius.
Filtering Data: FILTER

Extract names starting with the letter "E" from this updated list: Emma, Evan, Ella, Alice, Bob, Charlie, Diana, Fiona, George, Hannah.
Aggregating Data: REDUCE

Calculate the total of this list of numbers: 33, 87, 58, 46, 31, 29, 21, 40, 86, 47.'''

# Temperature converter:
temps=[32, -17, 40, 5, -7, 20, -1, 16, -16, 4]
converted = list(map(lambda x: ((x - 32) * 5/9), temps))
print(converted)

# Filtering names:
setnames= ["Emma", "Evan", "Ella", "Alice", "Bob", "Charlie", "Diana", "Fiona", "George", "Hannah"]
names_e= list(filter(lambda x : "E" in x , setnames ))
print(names_e)

# Using the reduce function to sum up numbers in a list:
from functools import reduce
nums= [33, 87, 58, 46, 31, 29, 21, 40, 86, 47]
sum_nums= reduce(lambda x, y: x+y, nums)
print(sum_nums)