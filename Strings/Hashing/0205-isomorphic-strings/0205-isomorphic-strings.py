class Solution(object):
    def isIsomorphic(self, s, t):
        map1={}
        map2={}
        for i in range(len(s)):
            c1=s[i]
            c2=t[i]
            if c1 in map1:
                if map1[c1]!=c2:
                    return False
            else:
                map1[c1]=c2
            if c2 in map2:
                if map2[c2]!=c1:
                    return False
            else:
                map2[c2]=c1
        return True