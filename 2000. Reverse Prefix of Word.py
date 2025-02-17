
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            A=word.index(ch)
            return word[0:A+1][::-1]+word[A+1::]
        else:
            return word


# word = "abcdefd"
# ch = "d"

word = "abcd"
ch = "z"
obj = Solution()
output = obj.reversePrefix(word,ch)

print(output)