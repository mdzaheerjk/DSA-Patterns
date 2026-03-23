class Solution(object):
    def firstUniqChar(self, s):
        hash_map={}
        for i in s:
            if i in hash_map:
                hash_map[i]+=1
            else:
                hash_map[i]=1
        for i in range(len(s)):
            if hash_map[s[i]]==1:
                return i
        return -1