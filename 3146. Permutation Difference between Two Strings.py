class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        index=0
        ans=0

        for i in s:
            a=t.find(i)
            ans+=abs(index-a)
            index+=1

        return ans

s = "abcde"
t = "edbac"
obj=Solution().findPermutationDifference(s,t)

print(obj)