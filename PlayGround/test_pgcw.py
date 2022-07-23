# product(p, q, … [repeat=1]) => cartesian product, equivalent to a nested for-loop
# => sample: product('ABCD', repeat=2) => result: AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
#
# add necessaire library to our code
import itertools as it
import test_service as ts


word_list = list(ts.get_words_from_usr())

start, end = ts.get_pass_range_from_user()


# open the pass-list file after the loops to avoide of repetitive action => reduce cpu usage
with open('PlayGround\\test.txt', 'w') as f:
    for i in range(start, end + 1):
        # get possible passwords by using itter.product function 
        prob_pass_list = list(it.combinations(word_list, i))
#
        # iterate over each pass-list built by 'product' function
        for j in range(len(prob_pass_list)):
#
            # building our string password by joining probable words in [j] index
            prob_pass_string = ''.join(prob_pass_list[j])
#
            # finally should write the password in specific file
            f.write(f"{prob_pass_string} \n")
#
