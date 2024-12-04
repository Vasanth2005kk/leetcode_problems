class Solution:
    def getPermutation(self, n: int, k: int) -> str:        
        output=[]
        start_Sequence=""
        for i in range(1,n+1):
            start_Sequence+=str(i)

        def swap(s, i, j):
            s = list(s)
            s[i], s[j] = s[j], s[i]
            return ''.join(s)

        def permuteRec(s, idx):
            if idx == len(s) - 1:
                output.append(s)
                return
            for i in range(idx, len(s)):
                s = swap(s, idx, i)
                permuteRec(s, idx + 1)
                s = swap(s, idx, i)

        def permute(s):
            permuteRec(s, 0)

        permute(start_Sequence)
        output.sort()
        return output[k-1]

n = 3
k = 5
obj = Solution().getPermutation(n,k)
print(obj)


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        from math import factorial
        numbers = list(map(str, range(1, n + 1)))
        k -= 1  # Convert k to 0-based index
        result = []

        for i in range(n):
            # Compute the index of the current digit
            fact = factorial(n - 1 - i)
            index = k // fact
            result.append(numbers[index])
            # Remove the used number and update k
            numbers.pop(index)
            k %= fact

        return ''.join(result)