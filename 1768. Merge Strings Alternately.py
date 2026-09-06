class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length1 = len(word1)
        length2 = len(word2)

        if length1 > length2:
            run = length1
        else:
            run = length2
        output = ""
        for i in range(run):
            if i <= length1-1:
                output += word1[i]
            if i <= length2-1:
                output += word2[i]
        return output
        
word1 = "ab"
word2 = "pqrs"

obj = Solution().mergeAlternately(word1,word2)
print(obj)