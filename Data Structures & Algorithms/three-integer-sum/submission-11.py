class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # so i am given an int array of nums
        # and i need to parst through it and return the sums of three unique elements in which they add up to 0 
        # NO DUPLICATES
        # return in any order

        # i dont think a hashmap will help me as i dont need to retrieve infomration 
        # using a stack doesnt make since cause i need to process elements not in order and find all of them

        # this means i probably just need to traverse the list

        # i could use two pointers and one pointer to traverse the list 
        # that algorithim would be O(n^2), the length of nums is very small though so i should be okay, this would also mean my alogrithim is O(1) space complexity
        # to effectively use two pointers in this way I need to sort the input 
        nums = sorted(nums)

        res = []

        for i in range(len(nums) - 2):
            if nums[i] > 0: 
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                val = nums[i] + nums[left] + nums[right]
                if val == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right: 
                        left += 1
                elif val < 0:
                    left += 1
                else:
                    right -= 1
        return res

        
        