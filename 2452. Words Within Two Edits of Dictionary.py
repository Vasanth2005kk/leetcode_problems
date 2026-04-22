from typing import List


class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        output = []
        stringlen = len(queries[0])
        zeros = 0
        for query in queries:
            if query in dictionary:
                output.append(query)
                continue

            for dic in dictionary:
                for index in range(stringlen):
                    if query[index] != dic[index]:
                        zeros +=1
                if zeros <=2 and query not in output:
                    output.append(query)
                zeros = 0

        return output
    
    

queries = ["word","note","ants","wood"]
dictionary = ["wood","joke","moat"]


obj = Solution().twoEditWords(queries,dictionary)
print(obj)