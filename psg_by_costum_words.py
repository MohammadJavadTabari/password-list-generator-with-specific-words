# just for tests
import itertools as it


itco = it.combinations([1,2,3,4,5], 3)
itcwr = it.combinations_with_replacement([1,2,3,4,5], r=3)
itac = it.accumulate([1,2,3,4,5])
itch = it.chain('ABCD', 'EFG', 'HIJK', 'LMNOP')
itcom = it.compress('ABCDEF', [1,0,1,0,1,1])
itsm = it.starmap(pow, [(2,5), (3,2), (10,3)])
itpr = it.product('ABCD', repeat=2)
itper = it.permutations('ABCD', 2)
a=0
##########################################
words = input('write your words with space:')
pass_lenth = input('What is the range length of the password? example 6-12:')
pass_lenth_range = pass_lenth.split('-')

words_list = words.split(' ')

list_combinations = list()
# consider duplicated words in combinations
for i in range(int(pass_lenth_range[0]), int(pass_lenth_range[1])):
    list_combinations += list(it.combinations(words_list, i))

print(list_combinations)