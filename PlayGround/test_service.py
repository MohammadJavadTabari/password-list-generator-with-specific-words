
# Get the possible password words from the user
def get_words_from_usr():
    words = input("type your words separated with space:")
    word_list = words.split(' ')
    return word_list


# Getting the possible password range from the user
def get_pass_range_from_user():
    pass_length = input('What is the range length of the password? example 6-12:')
    pass_length_range = pass_length.split('-')
    start = int(pass_length_range[0])
    end = int(pass_length_range[1])
    return start, end
