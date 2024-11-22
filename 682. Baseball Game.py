
class Solution:
    def calPoints(self, operations: List[str]) -> int:
                
        ans = []
        for i in operations:
            try:
                if int(i):
                    ans.append(int(i))
            except ValueError as e:
                if i == "C":
                    ans.pop()
                elif i == 'D':
                    ans.append(2*ans[-1])
                elif i == "+":
                    ans.append(ans[-2]+ans[-1])

        return sum(ans)



ops = ["5","-2","4","C","D","9","+","+"]

obj = Solution().calPoints(ops)