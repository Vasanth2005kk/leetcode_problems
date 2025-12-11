
class Solution:
    def validPalindrome(self, s: str) -> bool:
        for i in range(len(s)):
            slice_ = s[:i] + s[i+1:]
            if slice_ ==  slice_[::-1]:
                return True
        else:
            return False
s="abc"
solution = Solution()
print(solution.validPalindrome(s))  # Expected output: True


#ai 
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_pal(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                # try removing left or right character
                return is_pal(left + 1, right) or is_pal(left, right - 1)
            left += 1
            right -= 1

        return True


