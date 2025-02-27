class Solution:
    def groupAnagrams(self, strs):
        output = []
        unique = []

        for word in strs:
            sorted_word = "".join(sorted(word))  # Sort the word to create a unique key
            if sorted_word not in unique:
                unique.append(sorted_word)
                output.append([word])
            else:
                output[unique.index(sorted_word)].append(word)

        return output

strs = ["eat","tea","tan","ate","nat","bat"]
obj = Solution()
output = obj.groupAnagrams(strs)

print(output)