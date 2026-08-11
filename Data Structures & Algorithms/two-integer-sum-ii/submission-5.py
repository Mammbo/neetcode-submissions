class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # sorted in non decreasing order

        # is 1 index so add 1 at the end

        # find the targer by progressing towards the middle

        # one solution will be found
        left = 0 
        right = len(numbers) - 1

        while left < right:
            maybe_target = numbers[left] + numbers[right]

            if maybe_target == target: 
                return [left + 1, right + 1]
            elif maybe_target < target:
                left += 1
            else: 
                right -= 1