class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        ans=num+t
        return ans+t
        


num = 4
t = 1
obj =  Solution().theMaximumAchievableX(num,t)
print(obj)