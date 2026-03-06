class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        hash_map={}
        for i in s:
            if i in hash_map:
                hash_map[i]+=1
            else:
                hash_map[i]=1
        for j in t:
            if j in hash_map:
                hash_map[j]-=1
            else:
                hash_map[j]=1
        for key,values in hash_map.items():
            if values!=0:
                return False
        return True

        