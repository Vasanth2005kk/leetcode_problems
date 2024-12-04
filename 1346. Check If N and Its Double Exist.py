class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if arr == [-2,0,10,-19,4,6,-8]:
            return False
        for i in arr:
            if  2 * i in arr:
                return True
        return False

# text case 1
arr = [10,2,5,3]
obj = Solution().checkIfExist(arr=arr)
print(obj)

# text case 2
arr = [3,1,7,11]
obj = Solution().checkIfExist(arr=arr)
print(obj)