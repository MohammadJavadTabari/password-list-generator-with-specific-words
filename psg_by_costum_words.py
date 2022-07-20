from itertools import combinations

words = input('write your words with space:')
pass_lenth = input('What is the range length of the password? example 6-12:')
pass_lenth_range = pass_lenth.split('-')

words_list = words.split(' ')
list_combinations = list()
# consider duplicated words in combinations
for i in range(int(pass_lenth_range[0]), int(pass_lenth_range[1])):
    list_combinations += list(combinations(words_list, i))

print(list_combinations)