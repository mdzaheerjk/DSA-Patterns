class Solution(object):
    def searchInsert(self, nums, target):
        first=0
        last=len(nums)-1
        while first<=last:
            mid=(last+first)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                last=mid-1
            else:
                first=mid+1
        return last+1
        