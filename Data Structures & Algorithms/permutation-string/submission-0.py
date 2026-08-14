class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # i am given s1 and s2 
        # i must return true is s2 has the chars of s1 in it 
        # otherwise return false
        # this means it must be of length s1
        # to solve this problem i need to use a sliding window of fixed length
        seen = {}
        s1_map = {}
        k = len(s1)
        left = 0
        for i in range(k):
            s1_map[s1[i]] = 1 + s1_map.get(s1[i], 0)
        
        for right in range(len(s2)):
            seen[s2[right]] = 1 + seen.get(s2[right], 0)
            if right - left + 1 == k:
                if seen == s1_map: 
                    return True
                else:
                    seen[s2[left]] -= 1
                    if seen[s2[left]] == 0:
                        del seen[s2[left]]
                    left += 1
        return False
            

        


        

