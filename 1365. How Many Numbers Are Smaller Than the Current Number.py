
class Solution:
    def smallerNumbersThanCurrent(self,nums):        
        y=[]
        for i in nums:
            count=sum(1 for j in nums if j < i)
            y.append(count)

        return y
        # return y = [sum(1 for j in nums if j < i) for i in nums]c


nums = [8,1,2,2,3]
obj=Solution().smallerNumbersThanCurrent(nums=nums)
print(obj)


'''
nums = [8,1,2,2,3]

output=[]
total=0
for i in nums:
    for j in nums:
        if i > j:
            total+=1
    output+=[total]
    total=0

print(output)'''
