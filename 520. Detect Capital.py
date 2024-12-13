class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.islower() or word.istitle() or word.isupper():
            return(True)
        else:
            return(False)



word = "USA"
obj = Solution().detectCapitalUse(word)
print(obj)