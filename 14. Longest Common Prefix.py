strs = ["flower","flow","flight"]

class Solution:
    def longestCommonPrefix(self, strs):
        res = ""
        count=1
        for i in range(len(strs[0])):
            for s in strs:
                print(count,i == len(s) or s[i] != strs[0][i])
                count+=1
                if i == len(s) or s[i] != strs[0][i]:
                    return(res)
            res += strs[0][i]
        return(res)


obj=Solution().longestCommonPrefix(strs)
print(obj)