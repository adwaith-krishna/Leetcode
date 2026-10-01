class Solution:


    def isBadVersion(self, version):
        return version >= bad

    def firstBadVersion(self, n: int) -> int:
        left=0
        right=n
        

        while left<=right:
            mid=(left+right)//2

            if self.isBadVersion(mid):
                right=mid
            else:
                left=mid+1

        return left





a=Solution()

n = 5
print(a.firstBadVersion(n))

n = 1
print(a.firstBadVersion(n))