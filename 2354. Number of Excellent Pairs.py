from typing import List
class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        nums = list(set(nums))
        popcount = [bin(i).count("1") for i in nums]
                    
        print(popcount)
        total =0
        for i in popcount:
            for j in popcount:
                if i+j >=k:
                    total +=1

        return total


nums = [1,2,3,1]
k = 3

obj = Solution().countExcellentPairs(nums,k)
print(obj)

# ai code
''''
class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        # Step 1: Remove duplicates
        unique_nums = list(set(nums))
        
        # Step 2: Calculate popcount (number of 1s in binary)
        popcounts = [bin(num).count('1') for num in unique_nums]
        
        # Step 3: Sort the popcounts
        popcounts.sort()
        n = len(popcounts)
        total = 0

        # Step 4: Manual binary search
        def lower_bound(arr, target):
            left, right = 0, len(arr)
            while left < right:
                mid = (left + right) // 2
                if arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left

        # Step 5: For each popcount, find how many pairs satisfy the condition
        for count in popcounts:
            need = k - count
            idx = lower_bound(popcounts, need)
            total += n - idx  # count of valid j's such that count + popcounts[j] >= k

        return total
'''