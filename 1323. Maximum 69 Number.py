
class Solution:
    def maximum69Number (self, num: int) -> int:    
        num_str = str(num)
        output = [num]
        ans = ""

        for i in range(len(num_str)):
            if num_str[i] == "9":
                ans = num_str[0:i]+"6"+num_str[i+1::]
                output.append(int(ans))
            else:
                ans = num_str[0:i]+"9"+num_str[i+1::]
                output.append(int(ans))

        output.sort()
        return output[-1]
    
    
num = 9999
print(Solution().maximum69Number(num))