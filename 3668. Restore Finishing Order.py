class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        output = []
        for i in order:
            if i in friends:
                output.append(i)

        return output