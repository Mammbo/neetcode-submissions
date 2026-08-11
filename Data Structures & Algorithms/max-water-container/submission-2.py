class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # i am given the hiehgts the repersent where 
        # heights[i] repersents the ith bar

        # i think a two pointer solution could work

        max_water = 0

        left = 0
        right = len(heights) - 1

        while left < right: 
            total_water = (right - left) * min(heights[left], heights[right])
            max_water = max(max_water, total_water)

            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            else: 
                right -= 1
        return max_water
        

       



        