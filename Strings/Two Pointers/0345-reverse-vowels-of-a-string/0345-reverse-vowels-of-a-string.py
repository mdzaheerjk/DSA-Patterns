class Solution(object):
    def reverseVowels(self, s):
        vowels=['A','E','I','O','U','a','e','i','o','u']
        left=0
        right=len(s)-1
        s=list(s)
        while left<right:
            if not s[left] in vowels:
                left+=1
            elif not s[right] in vowels:
                right-=1
            elif s[right] in vowels and s[left] in vowels:
                s[left],s[right]=s[right],s[left]
                left+=1
                right-=1
        return "".join(s)
        