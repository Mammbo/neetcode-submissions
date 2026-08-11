class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # int array nums
        # return an array of triplets where they add up to 0

        # make sure i, j, and k are all distirct
        # no duplicate triplets should be stored in the res array
        res = []
        nums = sorted(nums)

        for i, a in enumerate(nums):
            if a > 0: 
                break
            if i > 0 and a == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                curr_sum = a + nums[left] + nums[right]
                if curr_sum == 0 and curr_sum not in res: 
                    res.append([a, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif curr_sum < 0:
                    left += 1
                else: 
                    right -= 1
        return res

        # this solution is O(n^2 because we iterating through the array at leasy twice) with O(1) space complexity because we arent adding else

        # using a hashmap would not improve the results of this because that would give us O(n) space and is basically the same algo
