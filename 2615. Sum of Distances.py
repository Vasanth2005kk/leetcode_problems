from typing import List

class Solution:
    def distance(self, nums: List[int]) -> List[int]:

        numsLenth = len(nums)
        output = []
        dis=0
        for index in range(numsLenth):
            # if nums.count(nums[index]) == 1:
            #     output.append(0)
            #     continue
            for j in  range(numsLenth):
                if nums[index] == nums[j] and index != j:
                    dis += abs(index-j)
            output.append(dis)
            dis = 0

        return output
    

nums = [1,3,1,1,2]

obj = Solution().distance(nums)

print(obj)



"ai"

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        index_map = {}
        
        # Group indices by value
        for i, num in enumerate(nums):
            if num not in index_map:
                index_map[num] = []
            index_map[num].append(i)

        output = [0] * n

        for indices in index_map.values():
            count = len(indices)
            prefix_sum = 0

            # Left pass
            for i, idx in enumerate(indices):
                output[idx] += idx * i - prefix_sum
                prefix_sum += idx

            # Right pass
            prefix_sum = 0
            for i in range(count - 1, -1, -1):
                idx = indices[i]
                right_count = count - 1 - i
                output[idx] += prefix_sum - idx * right_count
                prefix_sum += idx

        return output