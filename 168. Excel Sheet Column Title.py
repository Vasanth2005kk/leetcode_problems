class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        def num_hash(num):
            if num < 26:
                return alpha[num-1]
            else:
                q, r = num//26, num % 26
                if r == 0:
                    if q == 1:
                        return alpha[r-1]
                    else:
                        return num_hash(q-1) + alpha[r-1]
                else:
                    return num_hash(q) + alpha[r-1]

        return num_hash(columnNumber)

columnNumber = 2147483647

obj = Solution().convertToTitle((columnNumber))

print(obj)