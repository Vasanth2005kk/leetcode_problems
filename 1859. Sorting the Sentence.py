class Solution:
    def sortSentence(self, s: str) -> str:
        wordlist =  s.split()
        lenth = len(wordlist)

        output = [0]*lenth
        for word in wordlist:
            index = int(word[-1])-1
            value = word.strip("1234567890")
            output[index] =  value

        senteance =  " ".join(output)
        return  senteance


s = "is2 sentence4 This1 a3"
obj = Solution().sortSentence(s)

print(obj)