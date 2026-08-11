class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # now we are attempting three sum
        #i am given an integer array of nums 
        # return all the triplets where nums[i] + nums[j] + nums[k] == 0
        # i think what jumps to my mind is two pointers 
        # the output should not contain any duplicate triplets
        # so i have to check if there is duplcate triplets in the list
        # i am guaranteed for the array to be of three elements 
        # do i need to sort the array yes i need to if i am to implement two pointers in a predictable way 

        sortedNums = sorted(nums)
        setPointer = 0 
        res = []
        while len(sortedNums) - setPointer + 1 >= 3:
            right = len(sortedNums) - 1
            left = setPointer + 1 
            while left < right: 
                total = sortedNums[setPointer] + sortedNums[left] + sortedNums[right]
                if total > 0: 
                    right -= 1
                elif total < 0: 
                    left += 1
                else:
                    if list([sortedNums[setPointer], sortedNums[left], sortedNums[right]]) not in res:
                        res.append([sortedNums[setPointer], sortedNums[left], sortedNums[right]])
                    left += 1 
                    right -= 1
            setPointer += 1
        return res
        
            