class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # i am given an array of integers 
        # i must return the length of the longest consecutive sequence of elements that can be formed
        # a consecuritve sequence is sequence of elements in which each element is exactly 1 greater than the previous element 
        # element are NOT consecutive
        # ALGORTHIM MUST BE O(N) time 

        # so immedieatly thinking through thsi I think a hashset would be the ideally strategy
        # it gets rid of duplicates and allows O(1) access

        # i would iterate through nums however
        # if the value i am looking at has a previous element it is not a start of the sequence 
        # else it is and i start counting 
        hashset = set(nums)
        longest_sequence = 0
        for i in range(len(nums)): 
            # start of sequence
            val = nums[i]
            if val - 1 not in hashset:
                sequence = 0
                while val in hashset:
                    sequence += 1
                    val += 1
                longest_sequence = max(longest_sequence, sequence)
            else: 
                continue
        return longest_sequence
    


        