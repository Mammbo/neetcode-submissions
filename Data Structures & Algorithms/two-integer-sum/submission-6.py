class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # i am given an array of integers
        # i have a target integer
        # return the indicies i and j such that nums[i] + nums[j] == target and i != j
        # what i can do is store the keys (nums) and values ( indexes) in a hashmap and do a check of if target - current val is in hashmap. if i do that at every step i wont have to worry about i == j and i can do this in one pass with O(n) time complexity

        numMap = {}

        for i in range(len(nums)): 
            if target - nums[i] in numMap: 
                return [numMap[target - nums[i]], i]
            else: 
                numMap[nums[i]] = i
            
        
        