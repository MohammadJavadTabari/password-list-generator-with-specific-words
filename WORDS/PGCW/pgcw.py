# combinations(p, r) => r-length tuples, in sorted order, no repeated elements
# this file generate passwords by user words combinations with out replacement
import itertools as it

words = input("type your words separated with space:")
word_list = words.split(' ')

pass_length = input('What is the range length of the password? example 6-12:')
pass_length_range = pass_length.split('-')

list_combinations = list()

for i in range(int(pass_length_range[0]), int(pass_length_range[1])):
    list_combinations += list(it.combinations(word_list, i))

print(list_combinations)