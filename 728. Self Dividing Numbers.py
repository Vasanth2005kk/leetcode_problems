class Solution:
    def selfDividingNumbers(self, left: int, right: int):
        output = []
        while left <=  right :
            if left == 0:
                pass
            elif left < 9:
                output.append(left)
            else:
                if "0" in str(left):
                    pass
                else:
                    count = 0
                    for i in str(left):
                        if left % int(i) == 0:
                            count += 1
                    if count == len(str(left)):
                        output.append(left)
            left +=1
        return output

left = 0
right = 22

print(Solution().selfDividingNumbers(left,right))



class Solution:
    def selfDividingNumbers(self, left: int, right: int):
        output  =[]
        for i in range(left,right+1):
            if i < 10:
                output.append(i)
            else:
                if "0" not in str(i):
                    count =0 
                    for j in str(i):
                        if i % int(j) != 0:
                            break
                    else:
                        output.append(i)
        return output

left = 0
right = 22

print(Solution().selfDividingNumbers(left,right))