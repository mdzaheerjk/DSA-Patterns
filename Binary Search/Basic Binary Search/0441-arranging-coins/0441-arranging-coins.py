class Solution(object):
    def arrangeCoins(self, n):
        if n==1:
            return 1
        first=0
        last=n-1
        while first<=last:
            mid=(last+first)//2
            coin=(mid*(mid+1))//2
            if coin==n:
                return mid
            elif coin>n:
                last=mid-1
            else:
                first=mid+1
        return last

        