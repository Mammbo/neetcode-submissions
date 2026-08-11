class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # iterate through the list
        # if the complement num is not in hashmap add current val to hashmap
        # keep going until vals are found

        hashmap = {}

        for i in range(len(nums)):
            if target - nums[i] not in hashmap:
                hashmap[nums[i]] = i
            else:
                return [hashmap[target - nums[i]], i]
        