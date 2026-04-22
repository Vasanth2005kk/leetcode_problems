class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x=0
        y=0
        for i in moves:
            if i == "U":
                x+=1
            elif i == "D":
                x-=1
            elif i == "R":
                y+=1
            else:
                y-=1
            print(x,y)

        if x==0 and y ==0:
            return True
        return False

moves = "LDRRLRUULR"

obj = Solution().judgeCircle(moves)

print(obj)