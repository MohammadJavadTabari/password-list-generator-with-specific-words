# product(p, q, … [repeat=1]) => cartesian product, equivalent to a nested for-loop
# => sample: product('ABCD', repeat=2) => result: AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
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
with open('WORDS\PGPEW\pgpew_pass_list.txt', 'w') as f:
    for i in range(int(pass_length_range[0]), int(pass_length_range[1]) + 1):
#        
# get possible passwords by using itter.product function 
        prob_pass_list = list(it.product(word_list, i))
#
# iterate over each pass-list built by 'product' function
        for j in range(len(prob_pass_list)):
#
# building our string password by joining probable words in [j] index
            prob_pass_string = ''.join(prob_pass_list[j])
#
# finally should write the password in specific file
            f.write(f"{prob_pass_string} \n")