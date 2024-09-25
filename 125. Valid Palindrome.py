class Solution:
    def isPalindrome(self, s: str) -> bool:
        output=""
        for i in s:
            if i.isalnum():
                output+=i

        lowercase_letters= output.lower()

        if lowercase_letters == lowercase_letters[::-1]:
            return True
        else:
            return False

            