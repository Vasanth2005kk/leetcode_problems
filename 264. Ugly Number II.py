class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i2 = i3 = i5 = 0
        
        for _ in range(n - 1):
            next_ugly = min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5)
            ugly.append(next_ugly)
            
            if next_ugly == ugly[i2] * 2: 
                i2 += 1
            if next_ugly == ugly[i3] * 3: 
                i3 += 1
            if next_ugly == ugly[i5] * 5: 
                i5 += 1
        
        return ugly[-1]

n = 10
obj = Solution().nthUglyNumber(n)

print(obj)




# my code 

'''

n = 12
number = 2

if n == 1:
    print(1) 
prime_numbers =[7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
Ugly_number = [1,]
ans=0
while len(Ugly_number) <= n:
    if number % 2 == 0:
        ans = number
        Ugly_number.append(number)
    elif number % 3 == 0:
        ans = number
        Ugly_number.append(number)
    elif number % 5 == 0:
        ans = number
        Ugly_number.append(number)
    number +=1

    # print(ans)
    if ans > 12:
        chacking = []
        for i in range(2,ans+1):
            if ans % i == 0:
                if i in prime_numbers:
                    Ugly_number.remove(ans)
                    chacking.clear()
                    break
                else:
                   chacking.append(i)
        
        if chacking:
            Ugly_number.append(ans)

    Ugly_number = (list(set(Ugly_number)))

print((list(set(Ugly_number))))

'''