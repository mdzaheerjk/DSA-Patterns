class Solution(object):
    def groupAnagrams(self, strs):
        hash_map={}
        for i in strs:
            sorted_i="".join(sorted(i))
            if sorted_i in hash_map:
                hash_map[sorted_i].append(i)
            else:
                hash_map[sorted_i]=[i]
        return hash_map.values()        