"""
Morse Code Implementation to tell unique pattern

Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation: 
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".

Notes
The length of words will be at most 100.
Each words[i] will have length in range [1, 12].
words[i] will only consist of lowercase letters.
"""



def uniqueMorseRepresentations(words):

    import string

    unique_code = []

    if len(words) > 100:
        return -1

    letter_map = dict()
    letters = [letter for letter in string.ascii_lowercase]

    for count, letter in enumerate(morse_code_list):
        letter_map[letters[count]] = morse_code_list[count]

    for word in words:
        morse_code = ""
        for char in word:
            morse_code = morse_code + letter_map[char]
        if morse_code not in unique_code:
            unique_code.append(morse_code)

    return len(unique_code)


words = ["gin", "zen", "gig", "msg"]
print uniqueMorseRepresentations(words)