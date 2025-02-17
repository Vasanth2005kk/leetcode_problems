class Solution:
    def findCenter(self, edges) -> int:
        output = []
        for i in edges:
            output.extend(i)

        for i in output:
            if len(edges) == output.count(i):
                return i

edges = [[1,2],[2,3],[4,2]]

obj = Solution()
print(obj.findCenter(edges))