from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # i am given a group of strs
        # i need to group them all into sublist
        # i think what i can do is use a hashtable
        # i want to do it in one pass
        # i must create a key for each unique set of chars and use that key to append to a list

        hashmap = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            hashmap[tuple(count)].append(s)
        return list(hashmap.values())
        

                