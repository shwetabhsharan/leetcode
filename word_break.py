wordDict = ["cats", "dog", "sand", "and", "cat"]
def word_break(word):
    for w in wordDict:
        if w in word:
            print w
print word_break("catsandog")

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        for w in wordDict:
            if w in s:
                print s
                
