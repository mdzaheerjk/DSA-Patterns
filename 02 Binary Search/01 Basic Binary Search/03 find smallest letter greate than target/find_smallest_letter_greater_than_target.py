class Solution(object):
    def nextGreatestLetter(self, letters, target):
        first=0
        last=len(letters)-1
        answer=letters[0]
        while first<=last:
            mid=first+(last-first)//2
            if letters[mid]>target:
                answer=letters[mid]
                last=mid-1
            else:
                first=mid+1
        return answer