'''Practice Exercises:
List Transformation: Use map to create a list of the lengths of each word in the list ["Python", "Programming", "Is", "Fun"].

Filtering Values: Use filter to get all the prime numbers from a list [2, 3, 4, 5, 6, 7, 8, 9, 10].

Data Aggregation: Use reduce to concatenate a list of strings into a single sentence: ["Functional", "programming", "in", "Python"].'''

# List Transformation:
word_list= ["Python", "Programming", "Is", "Fun"]

new_list= list(map(lambda x: len(x), word_list))
print(new_list)

# Filtering Primes to a new list:
num_list= [2, 3, 4, 5, 6, 7, 8, 9, 10]

prime_list = list(filter(lambda x: all(x % i != 0 for i in range(2, int(x**0.5) + 1)) and x > 1, num_list))
print(prime_list)

# Concatenating a list:
from functools import reduce
word_list= ["Functional", "programming", "in", "Python"]

concat_list= reduce(lambda x, y: x + " " + y, word_list)
print(concat_list)
