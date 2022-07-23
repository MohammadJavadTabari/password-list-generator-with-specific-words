# product(p, q, … [repeat=1]) => cartesian product, equivalent to a nested for-loop
# this file generate passwords by user words combinations with out replacement
import itertools as it

words = input("type your words separated with space:")
word_list = words.split(' ')

pass_length = input('What is the range length of the password? example 6-12:')
pass_length_range = pass_length.split('-')

list_product = list()

for i in range(int(pass_length_range[0]), int(pass_length_range[1])):
    list_product += list(it.product(word_list, repeat=i))

print(list_product)