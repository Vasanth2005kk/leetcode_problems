class Solution:
    def sumOddLengthSubarrays(self, arr):
        n = len(arr)

        total=0
        for i in range(n):
            for j in (range(i,n)):
                if len(arr[i:j+1])%2 != 0:
                    total += sum(arr[i:j+1])
        
        return total



arr =[1,4,2,5,3]

obj = Solution().sumOddLengthSubarrays(arr)
print(obj)