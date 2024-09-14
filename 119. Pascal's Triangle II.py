class Solution:
    def getRow(self, rowIndex):
        rowIndex+=1
        nums_2=[None]*(rowIndex)

        index=0
        start=0
        end=2
        store=1

        for i in range(rowIndex):
            insert_list=[None]*(i+1)
            insert_list[0]=1
            insert_list[-1]=1

            if len(insert_list) == 3:
                insert_list[1]=2
            
            elif len(insert_list) > 3:

                for j in range(len(insert_list)-2):

                    ans=sum(nums_2[index-1][start:end])
                    insert_list[store]=ans

                    start+=1
                    end+=1
                    store+=1
                start=0
                end=2
                store=1

            nums_2[index]=insert_list
            index+=1        

        return nums_2[rowIndex-1]
    
obj = Solution().getRow(rowIndex=4)

print(obj)