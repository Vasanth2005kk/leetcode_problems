from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats = sorted(seats)
        students = sorted(students)

        MoveCount =0
        for i in range(len(seats)):
            MoveCount += abs(seats[i]-students[i])

        return MoveCount

seats = [3,1,5]
students = [2,7,4]

obj = Solution().minMovesToSeat(seats,students)
print(obj)