class Solution:
    def intToRoman(self, num: int) -> str:
        m = ["", "M", "MM", "MMM"]
        c = ["", "C", "CC", "CCC", "CD", "D",
            "DC", "DCC", "DCCC", "CM "]
        x = ["", "X", "XX", "XXX", "XL", "L",
            "LX", "LXX", "LXXX", "XC"]
        i = ["", "I", "II", "III", "IV", "V",
            "VI", "VII", "VIII", "IX"]
        
        thousands = m[num // 1000]
        hundreds = c[(num % 1000) // 100]
        tens = x[(num % 100) // 10]
        ones = i[num % 10]

        ans = (thousands + hundreds +
            tens + ones)

        return ans.replace(" ","")
    

obj=Solution().intToRoman(1994)
print(obj)

'''
# I,V,X,L,C,D,M =1,5,10,50,100,500,1000

num = 3749 #output = "LVIII"
roman=""

while num != 0:
    if num >=1000 and num <=3999:
        ans = num//1000
        num = num % 1000
        roman += "M"*ans
        print(num)
    elif num >=500 and num <=999:
        ans = num//500
        num = num % 500
        roman += "D"*ans
        print(num)
    elif num >=100 and num <=499:
        ans = num//100
        num = num % 100
        roman += "C"*ans
        print(num)
    elif num >=50 and num <=99:
        ans = num//50
        num = num % 50
        roman += "L"*ans
        print(num)
    elif num >=10 and num <=49:
        ans = num//10
        num = num % 10
        roman += "X"*ans
        print(num)
    elif num >=5 and num <=9:
        ans = num//5
        num = num % 5
        roman += "V"*ans
        print(num)
    else:
        ans = num//1
        num = num % 1
        roman += "I"*ans
        print(num)

roman=roman.replace("VIIII","IX").replace()

print(roman)



'''