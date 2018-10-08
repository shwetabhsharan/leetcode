"""
check_anagram(str1, str2)
get_all_anagrams(str1)
"""

def check_anagram(str1, str2):
    str1_data = [i for i in str1]
    str2_data = [i for i in str2]
    str1_data.sort()
    str2_data.sort()
    str1 = "".join(str1_data)
    str2 = "".join(str2_data)
    return str1 == str2

assert True == check_anagram("racecar", "carrace")
# assert True == check_anagram("racecar", "carrace1")

def get_all_anagram(str1):
    import itertools
    data = [i for i in str1]
    for item in itertools.permutations(data):
        print "".join(item)

get_all_anagram("str1")