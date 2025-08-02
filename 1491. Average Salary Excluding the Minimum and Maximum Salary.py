from typing import List
salary = [4000,3000,1000,2000]
class Solution:
    def average(self, salary: List[int]) -> float:
        total =0
        count =0
        salary.sort()
        for i in salary[1:-1]:
            total +=i
            count +=1

        return float(f"{total/count:.5f}")

salary = [4000,3000,1000,2000]
obj = Solution().average(salary)

print(obj)