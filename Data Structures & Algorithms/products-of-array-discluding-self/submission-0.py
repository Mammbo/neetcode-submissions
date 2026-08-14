class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       # i am given an int array nums
       # i must return an array output where output[i] is the product of all elements of nums except nums[i]

       # i think i can do this in two passes
        res = [1] * (len(nums))
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix 
            postfix *= nums[i]
        return res



            


        