class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:  
        # i am givne an array of integers
        # i need to return an int

        # i created a set of all possible nums so i am only looking at unique nums
        numSet = set(nums)
        longest = 0

        for num in numSet: 
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest


      