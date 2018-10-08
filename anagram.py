"""
Amagram is about creating permutations of the word
and checking if another word can be created out of it
"""

def check_anagram(str1, str2):
    str1_list = [i for i in str1]
    str2_list = [i for i in str2]
    str1_list.sort()
    str2_list.sort()
    if str1_list == str2_list:
        print "Strings are anagram to each other"
    else:
        print "Strings are not agagram to each other"

check_anagram("stackoverflow", "overflowstack")
check_anagram("stackoverflow", "overflowstack2")

def get_all_anagrams(str1):
    import itertools
    print ["".join(i) for i in itertools.permutations(str1)]

get_all_anagrams("shwetabh")