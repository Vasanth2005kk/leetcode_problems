class Solution:
    def convertTemperature(self, celsius):
        Kelvin = celsius + 273.15
        Fahrenheit = celsius * 1.80 + 32.00

        ans=[Kelvin,Fahrenheit]
        return ans


celsius = 36.50
obj=Solution().convertTemperature(celsius=celsius)

print(obj)