from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) > 2 :
            nums_min=  min(nums)
            num_max= max(nums)

            chacking = nums_min

            output = []
            ans=[]

            while chacking <= num_max+1:
                if chacking not in nums:
                    # print(chacking)
                    chacking += 1
                    if len(ans) == 1:
                        output.append(str(ans[0]))
                    else:
                        if not ans:
                            continue
                        output.append(f"{ans[0]}->{ans[-1]}")
                    ans =[]
                else:
                    ans.append(chacking)
                    chacking += 1
            
            return output
        else:
            if len(nums) ==  2:
                nums_min=  min(nums)
                nums_max= max(nums)
                
                if nums_min+1 == nums_max:
                    return [f"{nums_min}->{nums_max}"]
                else:
                    return [str(nums[0]),str(nums[1])]
            
            elif len(nums) == 1:
                return [str(nums[0])]
            return nums


nums = [0,5,9]
obj = Solution().summaryRanges(nums)
print(obj)

    
# ai
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        if not nums:
            return result
        
        start = nums[0]
        
        for i in range(1, len(nums)):
            # Break in sequence
            if nums[i] != nums[i - 1] + 1:
                # Single number
                if start == nums[i - 1]:
                    result.append(str(start))
                else:
                    result.append(f"{start}->{nums[i - 1]}")
                
                start = nums[i]
        
        # Add last range
        if start == nums[-1]:
            result.append(str(start))
        else:
            result.append(f"{start}->{nums[-1]}")
        
        return result
   