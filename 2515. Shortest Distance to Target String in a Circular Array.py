from typing import List

class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        
        if target in words:
            length =  len(words)
            right = 0
            left = 0

            for  i in range(length):
                if words[(i+startIndex)%length] == target:
                    break
                
                right +=1 
                

            for i in range(length):
                if words[(startIndex-i+length)%length]==target:
                    break

                left +=1 

            return min(right,left)

        return -1
    

words = ["ibkgecmeyx","jsdkekkjsb","gdjgdtjtrs","jsdkekkjsb","jsdkekkjsb","jsdkekkjsb","gdjgdtjtrs","msjlfpawbx","pbgjhutcwb","gdjgdtjtrs"]
target = "pbgjhutcwb"
startIndex = 0


obj = Solution().closestTarget(words,target,startIndex)
print(obj)