class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # i am given an array of integers
        # return the length of the longest consecutive sequence of elements that can be formed

        # i am making a hashmap where i am looking for a value 
        # the nums can be in any order
        # the algorithim must be in O(n) time so no sorting
        if len(nums) == 0: 
            return 0
        seen = set(nums) 
        ans = 0
        for value in seen:
            if value - 1 not in seen: 
                length = 1 
                while value + length in seen:
                    length += 1 
                ans = max(ans, length)
        return ans

