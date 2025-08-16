class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = [0]
        consonants  = [0]

        all_values = set(s)

        for i in all_values:
            if i in ['a','e','i','o','u']:
                vowels.append(s.count(i))
            else:
                consonants.append(s.count(i))

        return max(vowels) + max(consonants)
    
s = "successes"   

obj = Solution().maxFreqSum(s)
print(obj)