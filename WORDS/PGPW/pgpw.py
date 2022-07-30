# product(p, q, … [repeat=1]) => cartesian product, equivalent to a nested for-loop
# => sample: product('ABCD', repeat=2) => result: AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
#
# add necessaire library to our code
import WORDS.main_Services.common_actions_service as cas
import pgpw_service as pgpws

word_list = cas.get_words_from_usr()
start, end = cas.get_pass_range_from_user()
pgpws.product_function()(file_path='WORDS\PGPW\pgpw_pass_list.txt', word_list=word_list, start_range=start, end_range=end)