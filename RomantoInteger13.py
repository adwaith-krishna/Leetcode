class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        sum=0
        for char in s:
            if char in roman:
                val=roman[char]
            sum=sum+val

        return sum

a=Solution()
s = "III"
print(a.romanToInt(s))

s = "LVIII"
print(a.romanToInt(s))

s = "MCMXCIV"
print(a.romanToInt(s))