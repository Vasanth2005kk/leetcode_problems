class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        answer=""
        count=0
        while n != count:
            answer+=str(start)+"^"
            start+=2
            count+=1
                
        answer=answer.strip("^")
        # print(answer)
        return(eval(answer))  

n = 4
start = 3
obj=Solution().xorOperation(n=n,start=start)

print(obj)