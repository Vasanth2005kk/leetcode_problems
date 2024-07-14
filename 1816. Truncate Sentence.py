class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        string=s.split()
        return " ".join(string[0:k]).strip()


string="Hello how are you Contestant"
k = 4
obj=Solution().truncateSentence(s=string,k=k)

print(obj)


# class Solution:
#     def truncateSentence(self, s: str, k: int) -> str:
#         k_count=0
#         output=""
#         for i in s.split():
#             output+=i+" "
#             k_count+=1
#             if k == k_count:
#                 break

#         return output.strip()
    

# string="Hello how are you Contestant"
# k = 4
# obj=Solution().truncateSentence(s=string,k=k)

# print(obj)