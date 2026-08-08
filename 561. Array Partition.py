from typing import List
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:

        SortedNums = sorted(nums)
        total =0
        for index , value in enumerate(SortedNums):
            if index % 2 ==0:
                total += value

        return total

nums = [6,2,6,5,1,2]
obj = Solution().arrayPairSum(nums)
print(obj)


'''
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        numsMin = min(nums)
        numsMax = max(nums)
        k = numsMax - numsMin +1
        count = [0]*k

        for i in nums:
            index =  i - numsMin
            # print(f"value {i} index {index}")
            count[index] += 1

        # print(count)

        result = []
        for i in range(k):
            num = i + numsMin
            f = count[i]
            result.extend([num]*f)
            # print(f"number {num}")

        # print(result)
        total = 0
        iterator = 0
        for i in result:
            iterator +=1
            if iterator%2 ==1:
                total +=i
                # print("value",i)

        # print(f"Final Value : {total}")
        return total'''