class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        hash_map={}
        for i in ransomNote:
            if i in hash_map:
                hash_map[i]+=1
            else:
                hash_map[i]=1
        for j in magazine:
            if j in hash_map:
                hash_map[j]-=1
                if hash_map[j]==0:
                    del hash_map[j]
        return len(hash_map)==0