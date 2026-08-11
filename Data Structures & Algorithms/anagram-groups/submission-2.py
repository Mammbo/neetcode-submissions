class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # i am given an array of strings
        # group all anagrams together into sublists 
        # an anagram is a string that contains the exact saem characters as another string, but the order can be different
        # for this i want to make a hashmap
        # what am i mapping in that hashmap
        # i guess i store the sorted value of each of the strings and store only that once
        # then i can loop through the array and see if it is sorted store it in the array 
        # i can use sorting because the string length is from 0 to 100 so not that big 
        # the length cna be up to 1000 characters which again doesnt take that much time 

        groups = {}
        for i in strs: 
            if str(sorted(i)) not in groups: 
                groups[str(sorted(i))] = []
            groups[str(sorted(i))].append(i)
        return (list(groups.values()))