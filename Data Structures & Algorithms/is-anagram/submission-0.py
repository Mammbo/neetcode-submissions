class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # i am given two strings of s and t, 
        # return value is a boolean
        # anagram: exact same chars, but different order

        # create hashmaps 
        # if they do not equal each other return false


        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
    
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT