
from typing import List
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        
        output = []

        for i in range(len(words)):
            if x in words[i]:
                output.append(i)

        return output
words = ["abc","bcd","aaaa","cbc"] 
x = "a"


obj = Solution().findWordsContaining(words,x)
print(obj)