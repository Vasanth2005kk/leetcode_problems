class Solution:
    def finalValueAfterOperations(self, operations):
        ans=0

        for i in operations:
            if i in ["--X","X--"]:
                ans-=1
            else:
                ans+=1
            
        return ans
    
operations = ["X++","++X","--X","X--"]
    
obj=Solution().finalValueAfterOperations(operations)

print(obj)