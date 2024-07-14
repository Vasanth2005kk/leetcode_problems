# with loop 
class Solution:
    def fib(self, n: int) -> int:
        ans=[0,1]
        for i in range(2,n+1):
            ans.append(ans[i-2]+ans[i-1])
        return ans[n]
    
number=10
obj=Solution().fib(number)

print(obj)


# without loop

class Solution:
    def fib(self, n: int) -> int:
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return Solution().fib(n-1) + Solution().fib(n-2)
        
obj=Solution().fib(n=5)
print(obj)
