class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans=""
        for i in address:
            if "." == i:
                ans+="[.]"
            else:
                ans+=i
        return ans


address = "1.1.1.1"
obj=Solution().defangIPaddr(address=address)

print(obj)