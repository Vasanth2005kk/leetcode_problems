nums = [4,2,5,7]

class Solution:
    def sortArrayByParityII(self, nums):        
        odd = []
        even = []

        for i in nums:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)

        result = []
        for i in range(len(odd)):
            result.append(even[i])
            result.append(odd[i])
        return result