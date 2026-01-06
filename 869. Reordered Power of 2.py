import math
class Solution:
    def rearrangements(self,n):
        digits = list(str(n))
        result = set()

        def permute(path, used):
            if len(path) == len(digits):
                if path[0] != '0':              # no leading zero
                    result.add(int(''.join(path)))
                return

            for i in range(len(digits)):
                if used[i]:
                    continue
                used[i] = True
                permute(path + [digits[i]], used)
                used[i] = False

        permute([], [False] * len(digits))
        return list(result)


    def reorderedPowerOf2(self, n: int) -> bool:
        for i in self.rearrangements(n):
            if str(i).startswith('0') or str(i).endswith('0'):
                continue
            log2_value = math.log2(int(i))
            if log2_value.is_integer():
                return True
        return False
    

# ai 

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def count_digits(x):
            return sorted(str(x))

        target = count_digits(n)
        # print("Target digit count:", target)
        power = 1
        for _ in range(31):      # 2^0 to 2^30
            # print("Current power of 2:", power, "Digit count:", count_digits(power))
            if count_digits(power) == target:
                return True
            power <<= 1          # multiply by 2

        return False
    

obj = Solution()
print(obj.reorderedPowerOf2(128))  # True