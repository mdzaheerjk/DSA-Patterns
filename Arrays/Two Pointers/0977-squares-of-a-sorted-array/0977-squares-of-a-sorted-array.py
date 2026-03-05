class Solution(object):
    def sortedSquares(self, nums):
        i=0
        j=len(nums)-1
        k=len(nums)-1
        result=[0]*len(nums)
        while k>=0:
            a=nums[i]*nums[i]
            b=nums[j]*nums[j]
            if a>b:
                result[k]=a
                i+=1
            else:
                result[k]=b
                j-=1
            k-=1
        return result