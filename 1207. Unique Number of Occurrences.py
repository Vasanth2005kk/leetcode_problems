class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        output = []
        for i in set(arr):
            # print(i)
            output.append(arr.count(i))

        # print(output)

        lengh = len(output)
        unique_counts = len(set(output))


        if lengh != unique_counts:
            return False
        else:
            return True
