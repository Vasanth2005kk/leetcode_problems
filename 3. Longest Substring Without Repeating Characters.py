class Solution:
    def length_of_longest_substring(self,s: str) -> int:
        res_set=set()
        result=0
        l=0

        for i in range(len(s)):
            while s[i] in res_set:
                res_set.remove(s[i])
                l+=1
            res_set.add(s[i])
            result=max(result,i-l+1)
        return result
    
s="abcabcbb"
obj=Solution().length_of_longest_substring(s)
print(obj)

class Solution:
    def length_of_longest_substring(self,s: str) -> int:
        res_set=set()
        result=0
        l=0

        for i in range(len(s)):
            if s[i] in res_set:
                res_set.remove(s[i])
                l+=1
            res_set.add(s[i])
            result=max(result,i-l+1)
        return result
    
s="abcabcbb"
obj=Solution().length_of_longest_substring(s)
print(obj)


'''
        char_index_map = {}
        longest = 0
        start = 0

        for end, char in enumerate(s):
            if char in char_index_map and char_index_map[char] >= start:
                start = char_index_map[char] + 1
            char_index_map[char] = end
            longest = max(longest, end - start + 1)

        return longest
'''