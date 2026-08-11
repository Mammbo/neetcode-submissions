class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # array of integers numbers 
        # sorted in increasing order
        # i could make a hash map for this problem 
        # since it is two pointers though i think
        # i can just put one pointer at the end and increase it 
        # hashmap would be bad as it is O(n) additonal space meaning i need to traverse
        # the sum array in line 

        # i think i will use a left and right pointer to traverse the array 
        # THERE will always be one valid solution
        left = 0 
        right = len(numbers) - 1

        while left < right: 
            if numbers[right] + numbers[left] > target: 
                right -= 1
            elif numbers[right] + numbers[left] < target: 
                left += 1
            else: 
                break
        return [left + 1, right + 1]