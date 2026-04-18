class Solution:
    def selfDividingNumbers(self, left: int, right: int):
        output =[]
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