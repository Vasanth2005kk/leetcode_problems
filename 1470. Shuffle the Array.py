class Solution:
    def shuffle(self, nums ,n):

        ans_1=[]
        ans_2=[]
        count=0

        for i in nums:
            if n != count:
                count+=1
                ans_1.append(i)
            else:
                ans_2.append(i)
            
        output=[]
        for i ,j in zip(ans_1,ans_2):
            output.extend([i,j])

        return output

