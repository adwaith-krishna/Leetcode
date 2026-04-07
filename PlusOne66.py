class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        num = int("".join(map(str, digits)))
        num+=1
        arr = [int(i) for i in str(num)]

        return arr

a=Solution()
digits = [1,2,3]
print(a.plusOne(digits))

digits = [4,3,2,1]
print(a.plusOne(digits))