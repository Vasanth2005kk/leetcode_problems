class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        priceSort = sorted(prices)
        disSort =  sorted(discounts)
        disNum = len(discounts)
        priceNum = len(priceSort)
        if disNum > priceNum:
            h = priceNum
        else:
            h = disNum
        lastindex = -1
        output=[]
        for i in range(h):            
            d = (priceSort[lastindex] * (100 - disSort[lastindex]))/100
            lastindex -=1
            output.append(d)
        # print(output)
        index =0
        for i in range(len(priceSort)-disNum):
            output.append(priceSort[index])
            index+=1
        # print(output)
        result = f"{sum(output):.5f}"
        # print(result)
        return float(result)
            
            
        


obj = Solution()
prices = [10,30,21]
discounts = [50,60]

print(obj.minPrice(prices, discounts))  # Output: 470.00000