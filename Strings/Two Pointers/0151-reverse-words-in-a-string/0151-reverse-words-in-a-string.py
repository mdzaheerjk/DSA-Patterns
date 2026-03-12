class Solution(object):
    def reverseWords(self, s):
        s=s.split()
        first=0
        last=len(s)-1
        while first<last:
            s[first],s[last]=s[last],s[first]
            first+=1
            last-=1
        return " ".join(s)
