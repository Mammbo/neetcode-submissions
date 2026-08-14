class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # substring is a contingious range of chars 
        # we need to iterate through the list
        # i think from the title of this problem it is pretty obvious i need to just traverse the string seeing if it is a substring without repeating chars, i can use a sliding window for that 
        # the cool thing about sliding window is that since it is solving subproblems i can always be sure that error in the window i need to increase it by will be the left if the new right field is a repeating character

        seen = set()
        left = 0 
        longest_substring = 0 
        for right in range(len(s)): 
            while s[right] in seen: 
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            longest_substring = max(longest_substring, (right - left + 1))
        return longest_substring
        # looking at this complexity it would be O(n) since i only ever traverse the lenght of list 
        # o(1) mem because i am using constant vars 

        # run through a test case
        s="abcabcbb"
        l = a, 3
        r = c, 5
        longest_substring = 3
        # 
        