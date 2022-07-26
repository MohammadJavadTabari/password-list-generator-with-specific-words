# # combinations(p, r) => r-length tuples, in sorted order, no repeated elements
# # this file generate passwords by user words combinations with out replacement
# # => sample:combinations('ABCD', 2) => result: AB AC AD BC BD CD
#
# add necessaire library to our code
import Services.pgcw_main_service as pgcwms

word_list = list(pgcwms.get_words_from_usr())

start, end = pgcwms.get_pass_range_from_user()

pgcwms.combinations_functions(file_path='WORDS\PGCW\pgcw_pass_list.txt',
 start_range=start, end_range=end, word_list=word_list)
