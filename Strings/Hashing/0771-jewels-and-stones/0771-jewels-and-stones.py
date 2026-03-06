class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        counter=0
        hash_map={}
        for i in stones:
            if i in hash_map:
                hash_map[i]+=1
            else:
                hash_map[i]=1
        for j in jewels:
            if j in hash_map:
                counter+=hash_map[j]
        return counter
        
        