from typing import List
nums = ["325240361872","440618160237","785744447413","820980201297","470082520306","874146483840","425300857082","088636787077","813218016629","459000328006","188683382600"]

queries = [[6,7],[4,4],[1,8],[11,10],[4,8],[11,6],[1,1],[3,1],[11,10]]

#output [10,0,9,9,1,6,5,0,9]

'ai'
from typing import List

class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        output = []

        for k, trim in queries:
            arr = []

            # Step 1: Build (trimmed_value, index)
            for i, num in enumerate(nums):
                trimmed = int(num[-trim:])
                arr.append((trimmed, i))

            # Step 2: Sort by value, then index
            arr.sort(key=lambda x: (x[0], x[1]))

            # Step 3: Get k-th smallest (k-1 index)
            output.append(arr[k - 1][1])

        return output

obj = Solution().smallestTrimmedNumbers(nums,queries)
print(obj)


'''
class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        output = []
        index = 0

        for query in queries:
            dic = {}
            Store = []
            dic.clear()
            for j in nums:
                print(f"query {query} nums {j[int("-"+str(query[-1]))::]}")
                trimValue =  int(j[int("-"+str(query[-1]))::])
                # print("dic index values ",index)
                dic[index] = trimValue
                index +=1
                Store.append(trimValue)

            findvalue =  query[0]-1
            print("finded Value :",findvalue)
            print(dic)
            print(Store)
            Store.sort()
            for index,value in dic.items():
                if Store[findvalue] ==  value:
                    getValue = index
            print("getValue :",getValue)
            output.append(getValue)
            index = 0

        print("output",output)
'''