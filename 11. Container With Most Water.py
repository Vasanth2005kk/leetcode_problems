height = [1,8,6,2,5,4,8,3,7]
class Solution:
    def maxArea(self, height):    
        left=0
        right=len(height)-1
        result=0

        while left<right:
            destance=right-left
            min_number=min(height[left],height[right])
            store_water=destance*min_number

            if result < store_water:
                result=store_water
            elif height[left] > height[right]:
                right-=1
            else:
                left+=1
        return result

obj=Solution().maxArea(height=height)
print(obj)