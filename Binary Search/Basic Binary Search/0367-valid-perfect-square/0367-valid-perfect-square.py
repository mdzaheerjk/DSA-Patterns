class Solution(object):
    def isPerfectSquare(self, num):
        if num<2:
            return True
        first=0
        last=num//2
        while first<=last:
            mid=(first+last)//2
            square=mid*mid
            if num==square:
                return True
            elif square>num:
                last=mid-1
            else:
                first=mid+1
        return False
        