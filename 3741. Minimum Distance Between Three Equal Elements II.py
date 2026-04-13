from typing import List

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        
        dic = {}
        index = 0 

        for i in nums:
            if nums.count(i) >= 3:  
                if str(i) not in dic.keys():
                    dic[str(i)] = ""

                dic[str(i)] += str(index) + ","
            index += 1

        output = []

        for value in dic.values():
            indices = [int(x) for x in value.split(",") if x]
            
            for i in range(len(indices) - 2):
                a, b, c = indices[i], indices[i+1], indices[i+2]

                dist = abs(a - b) + abs(b - c) + abs(c - a)
                output.append(dist)

            print(value)

        if output:
            return min(output)
        
        return -1


# Test
nums = [5,3,5,5,5]
obj = Solution()
print(obj.minimumDistance(nums=nums))