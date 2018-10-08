"""
Longest palindromic substring
https://www.geeksforgeeks.org/manachers-algorithm-linear-time-longest-palindromic-substring-part-1/
Manachar's Algorithm
"""

class Solution(object):
    def __init__(self):
        self.wing_size = 0

    def longest_palindrome(self, s):
        # get the length of the string
        len_string = len(s)

        # if string length is 1 or reverse string matches, return palindrome
        if len_string <=1 or s == s[::-1]:
            return s

        res = ""

        for i in range(len_string):

            w = self.wing_size

            res = max(self.helper(s,i-w,i-w,w), self.helper(s,i-w,i-w+1,w), res, key=len)

            if (w>(len_string/2) and i>(len_string/2)):
                break

        return res

    def helper(self,s,l,r,w):

        count = 0

        while 0<=l and r < len(s) and s[l]==s[r]:
            l-=1; r+=1; count+=1

        self.wing_size = max(w, count)

        return s[l+1:r]