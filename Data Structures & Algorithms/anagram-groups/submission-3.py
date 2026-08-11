class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # i know i need to use a hashmap
        # if we copy the list, iterate through the list
        # and sort all values, we can store the valid words in there
        
        hashmap = {}
        for i in range(len(strs)):
            if ''.join(sorted(strs[i])) not in hashmap:
                hashmap[''.join(sorted(strs[i]))] = [strs[i]]
            else:
                hashmap[''.join(sorted(strs[i]))].append(strs[i])
        return list(hashmap.values())
                