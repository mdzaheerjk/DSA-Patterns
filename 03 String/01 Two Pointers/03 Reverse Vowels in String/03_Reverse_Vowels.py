class Solution(object):
    def reverseVowels(self, s):
        vowels=["A",'E','I','O','U','a','e','i','o','u']
        i=0
        j=len(s)-1
        lst=list(s)
        while i<j:
            if not lst[i] in vowels:
                i+=1
            elif not lst[j] in vowels:
                j-=1
            elif lst[i] in vowels and lst[j] in vowels:
                lst[i],lst[j]=lst[j],lst[i]
                i+=1
                j-=1
        return "".join(lst)  