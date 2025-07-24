from typing import List
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        answer = 0
        for i in accounts:
            total = sum(i)
            if total > answer:
                answer = total
        return answer
accounts = [[1,5],[7,3],[3,5]]
print(Solution().maximumWealth(accounts))

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        answer = 0
        total = 0
        for i in accounts:
            for j in i:
                total += j
            if total > answer:
                answer = total
            total = 0
        return answer

accounts = [[1,5],[7,3],[3,5]]
print(Solution().maximumWealth(accounts))