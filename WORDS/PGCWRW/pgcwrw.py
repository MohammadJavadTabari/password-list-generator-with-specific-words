# combinations_with_replacement(p, r) => r-length tuples, in sorted order, with repeated elements
# this file generate passwords by user words combinations with replacement
# => sample:combinations_with_replacement('ABCD', 2) => result: AA AB AC AD BB BC BD CC CD DD
#
# add necessaire library to our code
import itertools as it
#
# Getting the possible password words from the user
words = input("type your words separated with space:")
word_list = words.split(' ')
#
# Getting the possible password range from the user
pass_length = input('What is the range length of the password? example 6-12:')
pass_length_range = pass_length.split('-')
#
# open the pass-list file after the loops to avoide of repetitive action => reduce cpu usage
with open('WORDS\PGCWRW\pgcwrw_pass_list.txt', 'w') as f:
    for i in range(int(pass_length_range[0]), int(pass_length_range[1]) + 1):
#        
# get possible passwords by using itter.combinations_with_replacement function 
        prob_pass_list = list(it.combinations_with_replacement(word_list, i))
#
# iterate over each pass-list built by 'combinations_with_replacement' function
        for j in range(len(prob_pass_list)):
#
# building our string password by joining probable words in [j] index
            prob_pass_string = ''.join(prob_pass_list[j])
#
# finally should write the password in specific file
            f.write(f"{prob_pass_string} \n")
