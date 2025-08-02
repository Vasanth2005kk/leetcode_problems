
from typing import List

class Solution:
    def cellsInRange(self, s: str) -> List[str]:     
        s=s.split(":")     
        start = ord(s[0][0])
        start_number = int(s[0][1::])

        end = ord(s[-1][0])
        end_number = int(s[-1][1::])

        if start_number > end_number:
            min_value = end_number
            max_value = start_number
        else:
            min_value = start_number
            max_value = end_number

        output =[]
        for i in range(start,end+1):
            for j in range(min_value,max_value+1):
                # print()
                output.append(chr(i)+str(j))
        
        return output

s ="U7:X9"

obj = Solution().cellsInRange(s)

print(obj)