def reverse_string(word):
    """
        
    """
    # split chars in list
    char_list = [i for i in word]

    rev_char_list = []
    # iterate using negative index
    for i in range(len(word)-1, -1, -1):
        rev_char_list.append(char_list[i])
    print "".join(rev_char_list)

reverse_string("hello")