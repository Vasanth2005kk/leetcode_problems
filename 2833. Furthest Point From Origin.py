
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        right = 0
        left = 0
        output = []
        for move in ["L","R"]:
            for i in moves:
                if i == "L" or (i ==  "_" and move == "L"):
                    left +=1
                elif i == "R" or (i == "_" and move == "R"):
                    right +=1
            
            output.append(abs(right-left))
            right = 0
            left = 0 

        return max(output)
    
moves = "_______"

obj = Solution().furthestDistanceFromOrigin(moves)
print(obj)