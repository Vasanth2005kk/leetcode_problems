class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic={}
        output = []
        for i in ransomNote:
            dic[i]=ransomNote.count(i)
        for letter in dic:
            output.append(dic[letter] <= magazine.count(letter))
        
        return all(output)


ransomNote = "aa"
magazine = "aab"

obj = Solution()
output = obj.canConstruct(ransomNote,magazine)

print(output)